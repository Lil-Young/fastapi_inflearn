from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: float = 0.1

@app.post("/items/")
async def create_item(item: Item):
    return {"item": item.dict()}