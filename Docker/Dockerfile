FROM python:3.12

WORKDIR /solution

COPY requirements.txt .

RUN pip install -r requirements.txt

ENTRYPOINT ["jupyter", "notebook", "--port=8231", "--ip=0.0.0.0", "--allow-root"]
