#Importando la clase FastAPI
from fastapi import FastAPI
#Instanciando la clase FastAPI
app = FastAPI()

#path operation decoration
@app.get("/")
def home():
    return {"Hello": "World"}
#ejecutar usando uvicorn main:app --reload