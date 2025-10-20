"""
Field parameter for validation
"""
from fastapi import FastAPI, Query, Path, Body
from pydantic import BaseModel, Field

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = Field(None, title="description of the item", max_length=300)
    price: float = Field(..., gt=0, description="price of the item")

@app.put("/item/{item_id}")
def update_item(item:Item):
    return {"item": item}