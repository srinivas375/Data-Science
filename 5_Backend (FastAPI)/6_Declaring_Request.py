"""
Declare request example
"""

from fastapi import FastAPI, Query, Path, Body
from pydantic import BaseModel, Field, HttpUrl
from typing import List, Optional

app = FastAPI()


# way 1
# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None

#     model_config = {
#         "json_schema_extra": {
#             "example": {
#                 "name": "nani",
#                 "description": "A nice product",
#                 "price": 89.34,
#                 "tax": 12.2,
#             }
#         }
#     }



# Way 2
# class Item(BaseModel):
#     name: str = Field(..., examples=['srinu', 'nani', 'bantu'])
#     description: str = Field(..., examples=['A good product'])
#     price: float = Field(..., examples=[98.23])
#     tax: float = Field(..., examples=[1.2])

# Way 3
# giving examples inside a body

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

@app.put("/item/{item_id}")
def update_item(
    item_id: int,
    item: Item = Body(
        ...,
        openapi_examples={
            "example_1": {
                "summary": "Nice product",
                "description": "A simple example with nani",
                "value": {
                    "name": "nani",
                    "description": "A nice product",
                    "price": 89.34,
                    "tax": 12.2,
                },
            },
            "example_2": {
                "summary": "Worst product",
                "description": "Example with srinu",
                "value": {
                    "name": "srinu",
                    "description": "A worst product",
                    "price": 89.34,
                    "tax": 13.2,
                },
            },
            "example_3": {
                "summary": "Good product",
                "description": "Example with bablu",
                "value": {
                    "name": "bablu",
                    "description": "A good product",
                    "price": 23.34,
                    "tax": 1.2,
                },
            },
        },
    ),
):
    results = {"item_id": item_id, "item": item}
    return results