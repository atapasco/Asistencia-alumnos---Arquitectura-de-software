from fastapi import APIRouter
from config.bd import conn
from models.subject import subjects  
from schemas.subject import SubjectSchema
from typing import List
from starlette.status import HTTP_204_NO_CONTENT
from sqlalchemy import select

subject = APIRouter()

@subject.get(
    "/subjects",
    tags=["subjects"],
    response_model=List[SubjectSchema],
    description="Get a list of all subjects",
)
def get_subjects():
    return conn.execute(subjects.select()).fetchall()

@subject.post("/subject_post", tags=["subjects"], response_model=SubjectSchema, description="Create a new subject")
def create_subject(subject: SubjectSchema):
    new_subject = {
        "name": subject.name,
        "description": subject.description,
    }
    result = conn.execute(subjects.insert().values(new_subject))
    return conn.execute(subjects.select().where(subjects.c.id == result.lastrowid)).first()