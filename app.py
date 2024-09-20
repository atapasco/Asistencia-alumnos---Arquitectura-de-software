from fastapi import FastAPI
from routers.user import user
from routers.subject import subject
from routers.student import student
from routers.professor import professor 
from config.openAPI import tags_metadata

app = FastAPI(
    title="Users API",
    description="a REST API using python and mysql",
    version="0.0.1",
    openapi_tags=tags_metadata,
)

app.include_router(user)
app.include_router(subject)
app.include_router(student)
app.include_router(professor)