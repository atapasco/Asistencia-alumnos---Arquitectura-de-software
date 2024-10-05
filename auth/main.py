from fastapi import FastAPI
from src.auth import router as auth_router
from src.user import router as user_router
from config.openAPI import tags_metadata

app = FastAPI(
    title="Users API",
    description="a REST API using python and mysql",
    version="0.0.1",
    openapi_tags=tags_metadata,
)

app.include_router(auth_router)
app.include_router(user_router)
