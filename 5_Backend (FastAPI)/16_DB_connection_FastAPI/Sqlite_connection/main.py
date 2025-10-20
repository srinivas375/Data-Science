# run this main file

from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from database import engine, sessionLocal
from models import Base, User
from pydantic import BaseModel, EmailStr

app = FastAPI()

# create the table in database
Base.metadata.create_all(bind = engine)

# pydantic model to save user
class UserCreate(BaseModel):
    name: str
    email: EmailStr

# pydantic model for response
class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr

    model_config = {
        "from_attributes": True 
    }

# db session
def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root():
    return {"message": "Database and tables are ready"}

# getting user by id
@app.get("/users/{user_id}", response_model=UserResponse)
def read_user(user_id: int, db:Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

# get all users
@app.get("/users/", response_model=list[UserResponse])
def read_users(db:Session = Depends(get_db)):
    users = db.query(User).all()
    return users

@app.post("/users/")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = User(name = user.name, email = user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return JSONResponse(status_code=201, content={"id": db_user.id, "name": db_user.name, "email": db_user.email})

@app.put("/users/{user_id}", response_model=UserResponse)
def update_user(user_id: int, user:UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    db_user.name = user.name
    db_user.email = user.email

    db.commit()
    db.refresh(db_user)
    return db_user

#delete user
@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()

    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    
    db.delete(db_user)
    db.commit()
    return JSONResponse(status_code=200, content={"detail": f"User with id {user_id} deleted successfully"})