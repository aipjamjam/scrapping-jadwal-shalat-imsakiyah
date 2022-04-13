from pydantic import BaseModel, Field
from starlette.responses import JSONResponse


class req(BaseModel):
    city: str = Field(example="kota-bandung")


def success(label, data):
    res = {
        "status": True,
        "message": f"Get {label} successfull!",
        "data": data,
    }
    return JSONResponse(content=res, status_code=200)


def fail(label, status):
    res = {
        "status": False,
        "message": f"Get {label} unsuccessfull!",
        "data": None,
    }
    return JSONResponse(content=res, status_code=status)
