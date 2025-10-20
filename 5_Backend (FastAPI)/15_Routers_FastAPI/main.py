from fastapi import FastAPI
from routers import items, orders, users

app = FastAPI()

app.include_router(items.router)
app.include_router(orders.router)
app.include_router(users.router)

@app.get("/")
def root():
    return{"message": "Welcome to FastAPI"}