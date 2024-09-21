from pydantic import BaseModel
from typing import Optional

class ClassSchema(BaseModel):
    id: Optional[int]
    name: str
    professor: str
    subjet: int

    class Config:
        orm_mode = True