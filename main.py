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
