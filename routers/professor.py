from fastapi import APIRouter
from config.bd import conn
from models.professor import professors  # Asegúrate de tener el modelo de la tabla 'professors'
from schemas.professor import ProfessorSchema
from typing import List
from starlette.status import HTTP_204_NO_CONTENT
from sqlalchemy import select

professor = APIRouter()

@professor.get(
    "/professors",
    tags=["professors"],
    response_model=List[ProfessorSchema],
    description="Get a list of all professors",
)
def get_professors():
    return conn.execute(professors.select()).fetchall()

@professor.post("/profesor_post", tags=["professors"], response_model=ProfessorSchema, description="Create a new professor")
def create_professor(professor: ProfessorSchema):
    new_professor = {
        "id": professor.id,
        "user_email": professor.user_email,
        "name": professor.name,
        "birth_date": professor.birth_date,
    }
    result = conn.execute(professors.insert().values(new_professor))
    return conn.execute(professors.select().where(professors.c.id == result.lastrowid)).first()

@professor.get(
    "/professors/{id}",
    tags=["professors"],
    response_model=ProfessorSchema,
    description="Get details of a specific professor by ID",
)
def get_professor(id: str):
    return conn.execute(professors.select().where(professors.c.id == id)).first()

@professor.delete(
    "/professors/{id}",
    tags=["professors"],
    status_code=HTTP_204_NO_CONTENT,
    description="Delete a professor by ID",
)
def delete_professor(id: str):
    conn.execute(professors.delete().where(professors.c.id == id))
    return {"message": "Professor deleted successfully"}