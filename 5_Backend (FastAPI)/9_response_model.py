# response model, automatically validates the otuput
# it also used for filtering the outputs

from typing import Literal
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float = 11.6
    tags: list[str] = []

@app.post("/items/")
async def create_item(item: Item):
    return item

items = {
    "nani": {"name": "nani", "price": 34.5},
    "kalki": {"name": "kalki", "price": 35.89, "tax": 12.3},
    "bob": {"name": "bob", "price": 46.34, "tax": 11.6, "tags": []}
}


@app.get("/items/{item_id}", response_model=Item, response_model_exclude_unset=True)
async def read_item(item_id: Literal["nani", "kalki", "bob"]):
    return items[item_id]

@app.get("/items/{item_id}/name", response_model=Item, response_model_include={'name', 'price'})
async def read_item_name(item_id: Literal["nani", "kalki", "bob"]):
    return items[item_id]

@app.get("/items/{item_id}/public", response_model=Item, response_model_exclude={'price'})
async def read_item_public(item_id: Literal["nani", "kalki", "bob"]):
    return items[item_id]

class UserBase(BaseModel):
    username: str
    emai: EmailStr
    full_name: str | None = None

class UserIn(UserBase):
    password: str

class UserOut(UserBase):
    pass

@app.post("/user", response_model=UserOut)
async def create_user(user: UserIn):
    return user