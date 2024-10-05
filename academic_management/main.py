from fastapi import FastAPI
from src.course import router as course_router
from src.profesor import router as profesor_router
from src.student import router as student_router
from src.subject import router as subject_router
from config.openAPI import tags_metadata

app = FastAPI(
    title="Users API",
    description="a REST API using python and mysql",
    version="0.0.1",
    openapi_tags=tags_metadata,
)

app.include_router(course_router)
app.include_router(profesor_router)
app.include_router(student_router)
app.include_router(subject_router)