from fastapi import FastAPI
from src.profesor.router import professor as profesor_router
from src.student.router import student as student_router
from src.subject.router import subject_router
from config import tags_metadata

app = FastAPI(
    title="Users API",
    description="a REST API using python and mysql",
    version="0.0.1",
    openapi_tags=tags_metadata,
)

app.include_router(profesor_router)
app.include_router(student_router)
app.include_router(subject_router)