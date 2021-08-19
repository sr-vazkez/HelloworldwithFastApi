# Importando lo necesario
from fastapi import FastApi
from typing import Optional
# Hey mira se parece a flask
app = FastApi()
# Creando rutas


@app.get("/")
def read_root():
    return{"Hola": "Mundo"}


# Se usa el uvicorn main:app --reload para ejecutar esta wea
