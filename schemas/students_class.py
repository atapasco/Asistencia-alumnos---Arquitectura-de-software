from pydantic import BaseModel
from typing import Optional

class ClassStudentSchema(BaseModel):
    student_id: int
    class_id: int

    class Config:
        orm_mode = True