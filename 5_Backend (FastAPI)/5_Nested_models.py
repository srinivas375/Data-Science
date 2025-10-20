"""
Body - Nested models
"""

from fastapi import FastAPI, Query, Path, Body
from pydantic import BaseModel, Field, HttpUrl
from typing import List, Optional

app = FastAPI()


class Image(BaseModel):
    # url: str = Field(
    # ...,
    # pattern = r"^https?://(?:www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b(?:[-a-zA-Z0-9()@:%_\+.~#?&/=]*)$"
# )
    url: HttpUrl
    name: str

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: Optional[List[str]] = None  # or else, we can directly use list[str]
    image: list[Image] | None = None

class Offer(BaseModel):
    name: str
    description: str | None = None
    price: float
    items: list[Item]


@app.put("/item/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results

@app.post("/offers")
async def create_offer(offer: Offer):
    return offer

@app.post("/images/multiple")
async def create_mult_images(images: list[Image]):
    return images