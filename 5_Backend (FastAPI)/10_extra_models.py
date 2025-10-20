# this file covers the Extra models

from typing import Literal
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()

class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: str | None = None

class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None

class UserInDB(BaseModel):
    username: str
    hashed_password: str
    email: EmailStr
    full_name: str | None = None

def fake_pass_hasher(raw_pass: str):
    return f"supersecret{raw_pass}"


def fake_save_user(user_in: UserIn):
    hashed_password = fake_pass_hasher(user_in.password)
    user_in_db = UserInDB(**user_in, hashed_password=hashed_password)
    print("user saved.")
    return user_in_db

