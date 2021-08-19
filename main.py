# Importando lo necesario
from fastapi import FastAPI
from typing import Optional
# Hey mira se parece a flask
app = FastAPI()
# Creando rutas


@app.get("/")
def read_root():
    return{"Hola": "Mundo"}

# Creando una nueva ruta


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

# Se usa el uvicorn main:app --reload para ejecutar esta wea
