"""
Fast api is used to build lightweight API's, which runs faster and asynchronously to run the FastAPI file
Installing FastAPI: `pip istall fastapi[all]`
Run the FastAPI file: `uvicorn file_name:app_name arguments`
We have two arguments
  uvicorn 1_initial_file:app --ports = 8090   # we can define our own port
  uvicorn 1_initial_file:app --reload         # file reloads everytime, when changes were made
"""

from fastapi import FastAPI

app = FastAPI()

@app.get('/', description="This is the initial route executed, when the ")
async def greet():
    return {'message':'Welcome to FastAPI learning, hello from get call'}

@app.post('/')
async def wish():
    return {'message': 'Hello from post call'}

@app.put('/')
async def put():
    return {'message': 'Hello from put call'}

@app.delete('/')
async def delete():
    return {'message': 'Hello from delete call'}