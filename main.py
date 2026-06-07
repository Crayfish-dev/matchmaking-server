from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import random

app = FastAPI()

rooms = {}


class HostRequest(BaseModel):
    ip: str
    port: int


@app.post("/host")
def host_room(data: HostRequest):
    while True:
        code = str(random.randint(100000, 999999))
        if code not in rooms:
            break

    rooms[code] = {
        "ip": data.ip,
        "port": data.port
    }

    return {
        "code": code
    }


@app.get("/room/{code}")
def get_room(code: str):
    if code not in rooms:
        raise HTTPException(
            status_code=404,
            detail="Room not found"
        )

    return rooms[code]


@app.delete("/room/{code}")
def delete_room(code: str):
    if code in rooms:
        del rooms[code]

    return {
        "success": True
    }
