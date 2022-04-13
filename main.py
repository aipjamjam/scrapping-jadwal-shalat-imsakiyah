from curses import REPORT_MOUSE_POSITION
import json
from urllib import response
from fastapi import FastAPI
from src import _get_cities, _get_imsak_schedule, req, success, fail

app = FastAPI()


@app.get("/get-cities")
async def get_cities():
    response = _get_cities()
    if response is None:
        return fail("Cities", 500)
    return success("Cities", response)


@app.post("/get-imsak")
async def get_imsak(item: req):
    response = json.loads(_get_imsak_schedule(item.city))
    if response is None:
        return fail("Imsak", 400)
    return success("Imsak", response)
