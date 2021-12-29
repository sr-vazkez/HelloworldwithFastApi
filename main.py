#importar cosas de Python
from typing import Optional

#importando pydantic
from pydantic import BaseModel
""" Models
Que es un modelo?
representa un objecto en codigo del mundo real
pydantic es una libreria que nos permite crear modelos
"""
#Importando la clase FastAPI
from fastapi import FastAPI
from fastapi import Body
from fastapi import Query
#Instanciando la clase FastAPI
app = FastAPI()

#Models
class Persona(BaseModel):
    """ Models
    Con validaciones
    """
    nombre: str
    apellido: str
    edad: int
    color_cabello: Optional[str] = None 
    esta_casado: Optional[bool] = None     



@app.get("/")
def home():
    return {"Hello": "World"}

#Request y Response body 
@app.post("/persona/nueva")
def crear_persona(persona: Persona = Body(...)):
    return persona

#Validaciones Query Parameters

@app.get("/persona/detalle")
def mostrar_persona(
    nombre: Optional[str] = Query(None,  min_length=1, max_length = 50),
    edad: Optional[str] = Query(...)
    #deberia ser opcional, pero es para conocerlo de como debe ser obligatorio
):
    return {nombre: edad}