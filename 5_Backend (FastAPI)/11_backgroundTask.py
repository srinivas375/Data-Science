'''
BackgroundTasks 
    - It's a process that allowing you to execute functions after returning
      a response to the client without blocking the main request-response cycle. 
'''

from fastapi import FastAPI, BackgroundTasks

app = FastAPI()

def write_log(message: str):
    with open("log.txt", "a") as f:
        f.write(message + "\n")

@app.post("/send-message/")
async def send_message(message: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(write_log, f"Message sent: {message}")
    return {"message": "Message received"}