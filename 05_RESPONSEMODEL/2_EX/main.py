from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
@app.get("/item/", response_model=Item)
def get_item():
    return {"name": "milk", "price": 3.5, "tax": 2.5}
