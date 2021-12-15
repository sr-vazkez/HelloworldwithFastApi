#Importando la clase FastAPI
from fastapi import FastAPI
#Instanciando la clase FastAPI
app = FastAPI()

#path operation decoration
@app.get("/")
def home():
    return {"Hello": "World"}
#ejecutar usando uvicorn main:app --reload
#localhost:8000/docs para ver la documentacion 
#localhost:8000/redoc para ver la documentacion en una pagina web
""" Nota para entender de que va
paths es igual a routes / endpoints
operations es igual a methods 
4 operations 
get = traer 
post =  enviar
put = actualiza
delete = eliminar

otras operations
options = describir opciones de comunicacion para el destino
head = traer info de un doc pero sin el doc
patch = modificaciones parciales
trace = observar que le pasa a la peticion
"""
#path parameter obligatorios
#Query paramether ? son opcionales 
@app.get("/tweets/{tweet_id}")
def tweets(tweet_id: int):
    return {"tweet_id": tweet_id}
