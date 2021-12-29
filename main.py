#importar cosas de Python
from typing import Optional
from enum import Enum

#importando pydantic
from pydantic import BaseModel
from pydantic import Field
""" Models
Que es un modelo?
representa un objecto en codigo del mundo real
pydantic es una libreria que nos permite crear modelos
"""
#Importando la clase FastAPI
from fastapi import FastAPI
from fastapi import Body
from fastapi import Query, Path
#Instanciando la clase FastAPI
app = FastAPI()

#Models
class ColorCabello(Enum):
    white = "white"
    brown = "brown"
    black = "black"
    blonde = "blonde"
    red = "red"
class Location(BaseModel):
    city: str
    state: str
    country: str
class Persona(BaseModel):
    """ Models
    Con validaciones
    """
    nombre: str = Field(
        ...,
        min_length = 1,
        max_length = 50
        )
    apellido: str = Field(
        ...,
        min_length = 1,
        max_length = 50
        
        )
    edad: int = Field(
        ...,
        gt = 1,
        le = 115
        )
    color_cabello: Optional[ColorCabello] = Field(default = None)
    esta_casado: Optional[bool] = Field(default=None) 



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
    nombre: Optional[str] = Query(
        None,
        min_length=1, 
        max_length = 50,
        title="Nombre de la persona",
        description="Este es el nombre de la persona. Debe tener 1 y 50 caracteres"
        ),
    edad: Optional[str] = Query(
        ...,
        title = "Persona Edad",
        description = "Este es la edad de la persona. Es un parametro requerido"
        )
    #deberia ser opcional, pero es para conocerlo de como debe ser obligatorio
):
    return {nombre: edad}

"""Fast api tiene algo curioso 
en lugar de usar los famosos simnbolos, a su creador le parecio una buena idea usar palabras
>= ge = greater or equal than 
<= le = less or equal than
>  gt = greater than
< lt = less than

Los siguientes paramaetros son para mejorar la doc
title  
description 
"""
#Validaciones path Parameters
@app.get("/persona/detalle/{persona_id}")
def mostrar_persona(
    persona_id: int = Path(
        ...,
        gt=0
     )
    ): 
    return {persona_id: "It Exists!"}

#Validaciones: Request Body

@app.put("/persona/{persona_id}")
def update_person(
    persona_id: int = Path(
        ...,
        title= "Person ID",
        description="Este esl ID de la persona",
        gt=0
    ),
    persona: Persona = Body(...),
    location: Location = Body(...)
):
    results = persona.dict()
    results.update(location.dict())
    return results