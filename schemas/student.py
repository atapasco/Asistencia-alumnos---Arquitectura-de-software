from pydantic import BaseModel
from typing import Optional
from datetime import date

class StudentSchema(BaseModel):
    id: Optional[int]
    user_id: int
    name: str
    birth_date: date
    grade: int

    class Config:
        orm_mode = True
