from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel): # Pydantic 모델 정의
    name: str
    price: float
    is_offer: bool = None

@app.post("/items/")
def create_item(item: Item):
    return {"item": item.dict()} # Pydantic 모델을 API에 사용