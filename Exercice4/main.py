from typing import Union

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ou ["http://localhost:3000"] pour limiter
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

compteur = 0



@app.get("/")
def read_root():
    return {"Hello World server is running!"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/compteurPlus")
def lire_compteur_plus():
    global compteur
    compteur += 1
    return {"compteur": compteur}


@app.get("/compteurMoins")
def lire_compteur_moins():
    global compteur
    compteur -= 1
    return {"compteur": compteur}


@app.get("/GetCompteur")
def get_compteur():
    global compteur
    return {"compteur": compteur}



