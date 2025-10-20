"""
Body - Field
"""

from fastapi import FastAPI, Query, Path, Body
from pydantic import BaseModel

app = FastAPI()


@app.put("/items/{item_id}")
async def update_item(item_id: int, name:str = Body(...)):
    return {"item_id":item_id, "item": name}