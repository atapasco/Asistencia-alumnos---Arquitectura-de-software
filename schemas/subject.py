from pydantic import BaseModel
from typing import Optional

class SubjectSchema(BaseModel):
    id: Optional[int]
    name: str
    description: Optional[str]

    class Config:
        orm_mode = True