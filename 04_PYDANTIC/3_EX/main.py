from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import List

app = FastAPI()

class Item(BaseModel):
    name: str = Field(..., title="Item Name", min_length=2, max_length=50)
    description: str = Field(None, description="The description of the item", max_length=300)
    price: float = Field(..., gt=0, description="The price must be greater than zero")
    tag: List[str] = Field(default=[], alias="item_tags")

@app.post("/items/")
async def create_item(item: Item):
    return {"item": item.dict()}