# Importando lo necesario
from fastapi import FastAPI
from typing import Optional
# Hey mira se parece a flask
app = FastAPI()
# Creando rutas


@app.get("/")
def read_root():
    return{"Hola": "Mundo"}


# Se usa el uvicorn main:app --reload para ejecutar esta wea
