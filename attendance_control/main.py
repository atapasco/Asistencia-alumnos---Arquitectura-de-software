from fastapi import FastAPI
from src.attendance import router as attendance_router
from src.reporting import router as report_router
from src.notifications import router as notifications_router
from .config import tags_metadata

app = FastAPI(
    title="Users API",
    description="a REST API using python and mysql",
    version="0.0.1",
    openapi_tags=tags_metadata,
)

app.include_router(attendance_router)
app.include_router(notifications_router)
app.include_router(report_router)