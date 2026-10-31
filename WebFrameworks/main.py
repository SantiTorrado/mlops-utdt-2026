"""
MLOps - Aplicaciones Web
Tarea clase 26/10: rutas vistas en clase + endpoint de chistes (Official Joke API)

Correr con:
    fastapi dev main.py

Documentación interactiva en:
    http://127.0.0.1:8000/docs
"""
import random

import requests
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="MLOps - Web Frameworks TP")

OFFICIAL_JOKE_API_BASE = "https://official-joke-api.appspot.com"
# Categorias validas segun la documentacion de la Official Joke API
VALID_CATEGORIES = {"general", "programming", "knock-knock", "dad"}


# ---------------------------------------------------------------------------
# Rutas basicas vistas en clase
# ---------------------------------------------------------------------------

@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get("/goodbye")
def goodbye():
    return "Goodbye"


@app.get("/items/{item_id}")
def item(item_id: int):
    return {"item_id": item_id}


@app.get("/rand/{max}")
def rand(min: int = 0, max: int = 10):
    return f"Random number: {random.randint(min, max)}"


class Item(BaseModel):
    name: str
    price: float


@app.post("/create")
def create_item(item: Item):
    return f"New item created with name {item.name} and price {item.price}."


def model(x: float) -> float:
    return 3 * x + 1


class Features(BaseModel):
    x: float


@app.post("/predict")
def predict(features: Features):
    y = model(features.x)
    return {"prediction": y}


items = {1: "Item nro 1", 3: "Item nro 3"}


@app.get("/item/{item_id}")
def get_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return items[item_id]


# ---------------------------------------------------------------------------
# Endpoint pedido en la tarea: chistes aleatorios via Official Joke API
# https://official-joke-api.appspot.com/
#   - path param: cantidad de chistes (int)
#   - query param opcional: categoria (general, programming, knock-knock, dad)
# ---------------------------------------------------------------------------

@app.get("/jokes/{cantidad}")
def get_jokes(cantidad: int, categoria: str | None = None):
    if cantidad < 1:
        raise HTTPException(status_code=400, detail="La cantidad debe ser mayor a 0")

    if categoria is not None and categoria not in VALID_CATEGORIES:
        raise HTTPException(
            status_code=400,
            detail=f"Categoria invalida. Opciones validas: {sorted(VALID_CATEGORIES)}",
        )

    url = (
        f"{OFFICIAL_JOKE_API_BASE}/jokes/{categoria}/random"
        if categoria
        else f"{OFFICIAL_JOKE_API_BASE}/jokes/random"
    )

    chistes = []
    for _ in range(cantidad):
        response = requests.get(url, timeout=5)
        if response.status_code != 200:
            raise HTTPException(
                status_code=502, detail="Error consultando la Official Joke API"
            )
        # El endpoint /random de la API devuelve una lista con un solo chiste
        data = response.json()
        chistes.append(data[0] if isinstance(data, list) else data)

    return {"cantidad": cantidad, "categoria": categoria or "cualquiera", "chistes": chistes}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
