from fastapi import APIRouter, HTTPException
from .schemas import ProfessorSchema
from typing import List
from .service import (
    get_all_professors,
    create_new_professor,
    get_professor_by_id,
    delete_professor_by_id,
)

professor = APIRouter()

@professor.get(
    "/professors",
    tags=["professors"],
    response_model=List[ProfessorSchema],
    description="Get a list of all professors",
)
def get_professors():
    professors = get_all_professors()
    if not professors:
        raise HTTPException(status_code=404, detail="No professors found.")
    return professors

@professor.post(
    "/profesor_post",
    tags=["professors"],
    response_model=ProfessorSchema,
    description="Create a new professor"
)
def create_professor(professor: ProfessorSchema):
    new_professor = create_new_professor(professor)
    if new_professor is None:
        raise HTTPException(status_code=400, detail="Error creating professor.")
    return new_professor

@professor.get(
    "/professors/{id}",
    tags=["professors"],
    response_model=ProfessorSchema,
    description="Get details of a specific professor by ID",
)
def get_professor(id: str):
    professor = get_professor_by_id(id)
    if professor is None:
        raise HTTPException(status_code=404, detail="Professor not found.")
    return professor

@professor.delete(
    "/professors/{id}",
    tags=["professors"],
    status_code=204,
    description="Delete a professor by ID",
)
def delete_professor(id: str):
    if not delete_professor_by_id(id):
        raise HTTPException(status_code=404, detail="Professor not found or could not be deleted.")
    return {"message": "Professor deleted successfully"}