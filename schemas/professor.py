from pydantic import BaseModel
from typing import Optional
from datetime import date

class ProfessorSchema(BaseModel):
    id: str
    user_id: int
    name: str
    birth_date: date

    class Config:
        orm_mode = True