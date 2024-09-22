from fastapi import FastAPI
from routers.user import user
from routers.subject import subject_router
from routers.student import student
from routers.professor import professor 
from routers.class_management import class_router
from config.openAPI import tags_metadata

app = FastAPI(
    title="Users API",
    description="a REST API using python and mysql",
    version="0.0.1",
    openapi_tags=tags_metadata,
)

app.include_router(user)
app.include_router(subject_router)
app.include_router(student)
app.include_router(professor)
app.include_router(class_router)