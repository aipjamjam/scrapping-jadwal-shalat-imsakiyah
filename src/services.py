from pydantic import BaseModel, Field

class req(BaseModel):
    city: str = Field(example="kota-bandung")