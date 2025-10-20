"""
Body - Multiple parameters
"""

# if we want a parameter to be in request body, it should be a BaseModel type
# or we can use the "Body" object

from fastapi import FastAPI, Query, Path, Body
from pydantic import BaseModel

# declaring the app
app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None # we can also use 'Optional' 
    price: float
    tax: float | None = None

class User(BaseModel):
    username: str
    branch: str

@app.put("/items/{item_id}")
def update_item(
    *, # so all next after * should be keyword arguments, but not positonal arguments
    item_id: int = Path(..., description="The id of the item to get", gt=0, lt=150),
    q: str | None = None,
    item: Item | None = None,
    user: User,
    importance:int =  Body(..., embed=True)
):
    results = {"item_id": item_id}
    if q:
        results.update({"q":q})
    if item:
        results.update({"item": item})
    if user:
        results.update({'user':user})
    if importance:
        results.update({'importance': importance})
    return results