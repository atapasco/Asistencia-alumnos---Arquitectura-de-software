from pydantic import BaseModel
from typing import Optional

class ClassSchema(BaseModel):
    id: str
    name: str
    professor: int
    subject: int

    class Config:
        orm_mode = True