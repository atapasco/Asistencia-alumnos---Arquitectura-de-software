from fastapi import FastAPI
from src.user.router import user as user_router
from config import tags_metadata
import uvicorn

app = FastAPI(
    title="Users API",
    description="a REST API using python and mysql",
    version="0.0.1"
)

app.include_router(user_router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001) 