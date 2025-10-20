from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime, time, timedelta

app = FastAPI()

class ProcessParams(BaseModel):
    start_date: datetime | None = None
    end_date: datetime | None = None
    repeat_at: time | None = None
    process_after: timedelta | None = None

@app.put("/items/{item_id}")
async def read_items(item_id: UUID, params: ProcessParams):
    start_process = (
        params.start_date + params.process_after
        if params.start_date and params.process_after
        else None
    )
    duration = (
        params.end_date - start_process
        if params.end_date and start_process
        else None
    )
    return {
        "item_id": item_id,
        "start_process": start_process,
        "duration": duration,
    }
