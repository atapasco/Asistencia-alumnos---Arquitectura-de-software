from fastapi import APIRouter
from config.bd import conn
from models.student import students  # Asegúrate de tener el modelo de la tabla 'students'
from schemas.student import StudentSchema
from typing import List
from starlette.status import HTTP_204_NO_CONTENT
from sqlalchemy import select

student = APIRouter()

@student.get(
    "/students",
    tags=["students"],
    response_model=List[StudentSchema],
    description="Get a list of all students",
)
def get_students():
    return conn.execute(students.select()).fetchall()

@student.post("/student_post", tags=["students"], response_model=StudentSchema, description="Create a new student")
def create_student(student: StudentSchema):
    new_student = {
        "user_email": student.user_email,
        "name": student.name,
        "birth_date": student.birth_date,
        "grade": student.grade,
    }
    result = conn.execute(students.insert().values(new_student))
    return conn.execute(students.select().where(students.c.id == result.lastrowid)).first()

