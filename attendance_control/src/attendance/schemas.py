from pydantic import BaseModel
from typing import Optional
from datetime import date

class AttendanceSchema(BaseModel):
    id: Optional[int]
    student_id: int
    class_id: int
    date: date
    status: str