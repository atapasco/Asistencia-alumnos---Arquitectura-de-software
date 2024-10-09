from fastapi import FastAPI
from src.attendance.router import attendance_router
from src.reporting import router
from src.notifications import router 
from config import tags_metadata

app = FastAPI(
    title="Users API",
    description="a REST API using python and mysql",
    version="0.0.1"
)

app.include_router(attendance_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8002)