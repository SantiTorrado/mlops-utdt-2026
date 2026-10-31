# MLOps (Aplicaciones Web) - UTDT

Repo de prácticas personales de la materia. Docentes: Agustín Mosteiro, Federico Pousa, Roni Barylko.

## Entorno
- **Fuente de verdad del código**: `~/code/mlops-utdt-2026` dentro de **WSL2 Ubuntu 26.04** (NO la copia vieja en OneDrive de Windows, quedó desactualizada y sin git).
- Usuario WSL: `santi`, sudo sin password (conveniencia dev). Docker Engine nativo corriendo vía systemd, sin necesidad de `sudo docker`.
- VS Code conectado vía extensión Remote-WSL. Para laburar: abrir VS Code → `Ctrl+Shift+P` → "WSL: Connect to WSL" → Open Folder → `/home/santi/code/mlops-utdt-2026`.
- GitHub: repo público `SantiTorrado/mlops-utdt-2026`, auth por SSH ya configurada.
- Cada carpeta de práctica tiene su propio venv local (no commiteado). PDFs de la cátedra excluidos del repo por derechos de autor.

## Cronograma de la materia
| Fecha | Tema | Estado |
|---|---|---|
| 19/10 | Intro: Linux, AWS, SSH, Streamlit, Gradio, Docker, Git, Venvs | ✅ visto |
| 26/10 | Servidores/protocolos web: cliente-servidor, Web Frameworks (FastAPI), Web Servers | ✅ visto |
| 31/10 | **Clase práctica 1** | ✅ hecha (TP FastAPI) |
| 02/11 | Automatización de tareas: orquestación de workflows, Airflow | ⏳ pendiente |
| 09/11 | Desarrollo cloud: AWS EC2, RDS, AppRunner, S3 | ⏳ pendiente |
| 16/11 | Herramientas de deployment avanzadas, casos reales | ⏳ pendiente |
| 02/12 | **Clase práctica 2** | ⏳ pendiente |

**TP Final**: grupal, exactamente 4 personas sin excepción. Requiere inscripción previa por formulario en el campus. Estado: sin grupo armado todavía.

## Estado del setup técnico (checklist)
- [x] WSL2 + Ubuntu 26.04, systemd habilitado
- [x] Docker Engine nativo, probado con `hello-world` y con la imagen real del curso (`Docker/Dockerfile`, Jupyter)
- [x] Git + SSH contra GitHub
- [x] VS Code + Remote-WSL
- [x] `WebFrameworks/` - TP de FastAPI completo: rutas de clase + endpoint `/jokes/{cantidad}?categoria=` contra la Official Joke API. Probado end-to-end.
- [x] `Gradio/text-2-speech/` - probado, corre en `:7860`
- [x] `Streamlit/text-to-speech/` - probado, corre en `:8501`
- [ ] `Gradio/image-2-speech/` (OCR + texto a voz) - dependencias instaladas (incl. `tesseract-ocr` del sistema), falta probarlo end-to-end
- [ ] `Streamlit/visualize-PCA/` - código listo, **falta el dataset** (ver pendientes)
- [x] `TelegramBot/` - token sacado del código, movido a `.env` (gitignored) vía `python-dotenv`. **El token viejo sigue potencialmente expuesto** hasta que se revoque.

## Pendientes - acción del usuario (Santi)
1. **Revocar el token viejo del bot de Telegram.** Vía la app de Telegram (no es nada de terminal): abrir chat con `@BotFather` → mandar `/mybots` → elegir el bot → `Bot Settings` → `API Token` → `Revoke current token`. Pegar el token nuevo en `TelegramBot/.env` (variable `TELEGRAM_BOT_TOKEN`, ese archivo nunca se commitea). Pendiente, deprioritizado por el usuario por ahora.
2. **Descargar el dataset de Kaggle "Digit Recognizer"** (`train.csv`, `test.csv`) desde `kaggle.com/c/digit-recognizer/data` y ponerlo en `~/code/mlops-utdt-2026/MNIST/` (carpeta nueva, al mismo nivel que `Streamlit/` y `VirtualEnv/`) para que funcione `Streamlit/visualize-PCA/app.py`.
3. **Crear cuenta de AWS** en `portal.aws.amazon.com/billing/signup` (pide tarjeta de crédito válida aunque no se gaste, entra en free tier). Necesaria antes del 9/11. OJO con dejar servicios prendidos sin supervisión (factura).
4. **Armar grupo de 4 para el TP Final** e inscribirse por el formulario del campus.

## Próximos pasos sugeridos (en este orden, cuando se retome)
1. Probar `Gradio/image-2-speech/` end-to-end (subir una imagen con texto, confirmar que el audio se genera bien).
2. Si ya está el dataset de Kaggle, probar `Streamlit/visualize-PCA/`.
3. Confirmar si se revocó el token de Telegram; si sí, probar el bot end-to-end (requiere un chat real de Telegram para probarlo, no se puede automatizar del todo).
4. Cuando la cátedra suba el material de la clase del 2/11 (Airflow): instalar Airflow vía Docker Compose dentro de WSL, siguiendo el material nuevo.
5. Guiar la creación de cuenta de AWS + primera instancia EC2 + conexión SSH (ya existe un par de claves en `~/.ssh/id_ed25519` dentro de WSL, usada para GitHub; para AWS probablemente venga un `.pem` nuevo que da la cátedra/la cuenta).
6. Cuando haya grupo para el TP Final: armar un repo GitHub aparte específico para eso (no mezclar con este repo de prácticas individuales), agregar a los 4 como colaboradores, trabajar con ramas + PRs.

## Notas técnicas
- Trabajar siempre desde `~/code/...` dentro de WSL, nunca desde `/mnt/c/...` (mucho más lento).
- `*.pdf` está en `.gitignore` a propósito (material de cátedra, no redistribuir en repo público).
- Para correr cualquier app: `cd <Carpeta>/<subcarpeta> && source ../venv/bin/activate && python app.py` (o `streamlit run app.py` / `fastapi dev main.py` según corresponda).
