# Importando lo necesario
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
# Hey mira se parece a flask
app = FastAPI()
# Creando rutas


class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None


@app.get("/")
def read_root():
    return{"Hola": "Mundo"}

# Creando una nueva ruta


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

# Se usa el uvicorn main:app --reload para ejecutar esta wea


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
         return {"item_name": item.name, "item_id": item_id}
