from fastapi import FastAPI
from typing import Union
from pydantic import BaseModel

app = FastAPI()

class Cat(BaseModel):
    catname: str

class Dog(BaseModel):
    dogname: str

@app.get("/animal/", response_model=Union[Cat, Dog])
async def get_animal(animal: str):
    if animal == 'cat':
        return {'catname':'Whiskers'} # Cat(name='Whiskers')
    else:
        return {'dogname': 'Fido'} # Dog(name=('Fido'))
