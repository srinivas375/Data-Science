# created a local json data (users data) (works as database, used for crud operations)
# in this file, we will learn to get the entire data, data by id
# order of defining the routes is important while coding

# there are examples containing path parametes, query parameters

# Path - used for path parameters
# Query - used for Query parameters

# Post request is used to create a user using pydantic module
# Put request is used ot update a user data using pydantic and fastapi

# deleting the user


from fastapi import FastAPI, Path, HTTPException, Query
from typing import Literal, Annotated, Optional
import os
import json
from enum import Enum
from pydantic import BaseModel, Field
from fastapi.responses import JSONResponse


# loading the data to display
def load_data():
    users_path = './data/users.json'
    if os.path.exists(users_path):
        with open(users_path, 'r') as f:
            return json.load(f)
    else:
        return HTTPException(status_code=404, detail="No such DB exists")

def save_data(data):
    with open('./data/users.json', 'w') as f:
        json.dump(data, f)

#user data structure
class User_data(BaseModel):
    id: Annotated[str, Path(..., description="id of the person, should be unique")]
    name:str
    age:Annotated[int, Path(..., gt=1, lt=150)]
    city:str
    occupation:str
    smoker:bool

# updating the user structure
class Update_user_data(BaseModel):
    name: Annotated[Optional[str], Field(default=None)]
    age: Annotated[Optional[int], Field(default=None)]
    city: Annotated[Optional[str], Field(default=None)]
    occupation: Annotated[Optional[str], Field(default=None)]
    smoker: Annotated[Optional[bool], Field(default=None)]

#loading the app
app = FastAPI()

#home path
@app.get('/')
async def home():
    return {'message':'Welcome to the users management system'}


@app.get('/users')
async def get_all_users(
    limit: int = Query(None, description="Limit the users to be displayed"),
    smoker: bool = Query(None, description="Filter based on smoker status")
):
    data = load_data()
    users_list = list(data.values()) 

    if smoker is not None:
        users_list = [user for user in users_list if user["smoker"] == smoker]

    if limit:
        users_list = users_list[:limit]

    return users_list

#getting specific users data
@app.get('/users/{id}')
async def get_user(id:str = Path(..., description="Enter the id of the User", example=23)):
    data = load_data()
    if id in data:
        return data[id]
    return HTTPException(status_code=404, detail="No user Found")


# defining a Enum type 
class FoodEnums(str, Enum):
    fruits = 'fruits'
    vegetables = 'vegetables'
    dairy = 'dairy'

@app.get('/foods/{food_name}')
def get_food(food_name:FoodEnums):
    if food_name == FoodEnums.vegetables:
        return {"food_item":food_name, "message": "You are healthy"}
    elif food_name.value == 'fruits':
        return {'food_item':food_name, "message": "You are still healthy"}
    return {'food_item':food_name, 'message': "Eat healthy food"}


@app.post('/add_user')
def create_user(user:User_data):
    data = load_data()

    if user.id in data:
        raise HTTPException(status_code=400, detail="User data already exists")
    data[user.id] = user.model_dump(exclude=['id'])

    save_data(data)

    return JSONResponse(status_code=201, content={'message':'user created successfully'})

@app.put('/update_user/{id}')
def update_user(id:str, modified_user_data:Update_user_data):
    data = load_data()
    if id not in data:
        raise HTTPException(status_code=404, detail="Patient details not found")
    exist_user_info = data[id]
    got_user_info = modified_user_data.model_dump(exclude_unset=True)
    for key, val in got_user_info.items():
        exist_user_info[key] = val
    data[id] = exist_user_info
    save_data(data)
    return JSONResponse(status_code=200, content={'message':'User data Updated'})



@app.delete('/delete_user/{id}')
def delUserInfo(id:str):
    data = load_data()
    if id not in data:
        raise HTTPException(status_code=404, detail="User not found")
    del data[id]
    save_data(data)
    return JSONResponse(status_code=200, content={'Message':'User deleted'})