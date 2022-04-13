import json
from fastapi import FastAPI
from src import _get_cities, _get_imsak_schedule, req

app = FastAPI()

@app.get("/get-cities")
async def get_cities():
    return {
        "status": True,
        "message": "Get cities successfull!",
        "data": _get_cities(),
    }


@app.post("/get-imsak")
async def get_imsak(item: req):
    data = json.loads(_get_imsak_schedule(item.city))
    return {
        "status": True,
        "message": "Get Imsak successfull!",
        "data": data,
    }
