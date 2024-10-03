from fastapi import APIRouter, HTTPException
from service.student_service import get_all_students, create_new_student
from schemas.student import StudentSchema
from typing import List

student = APIRouter()

@student.get(
    "/students",
    tags=["students"],
    response_model=List[StudentSchema],
    description="Get a list of all students",
)
def get_students():
    # Llama al servicio para obtener todos los estudiantes
    students = get_all_students()
    if not students:
        raise HTTPException(status_code=404, detail="No students found.")
    return students

@student.post(
    "/student_post",
    tags=["students"],
    response_model=StudentSchema,
    description="Create a new student"
)
def create_student(student: StudentSchema):
    # Llama al servicio para crear un nuevo estudiante
    new_student = create_new_student(student)
    if new_student is None:
        raise HTTPException(status_code=400, detail="Error creating student.")
    return new_student