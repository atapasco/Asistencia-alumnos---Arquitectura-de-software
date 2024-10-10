from fastapi import APIRouter, HTTPException
from typing import List
from .schemas import AttendanceSchema
from .service import (
    register_attendance_service,
    update_attendance_service,
    get_attendance_for_class_service
)

attendance_router = APIRouter()

@attendance_router.post(
    "/classes/{class_id}/attendance/",
    tags=["attendance"],
    response_model=AttendanceSchema,
    description="Register attendance for a specific class"
)
def register_attendance(class_id: int, attendance_data: AttendanceSchema):
    return register_attendance_service(class_id, attendance_data)


@attendance_router.put(
    "/attendance/{attendance_id}",
    tags=["attendance"],
    response_model=AttendanceSchema,
    description="Update attendance record"
)
def update_attendance(attendance_id: int, attendance_data: AttendanceSchema):
    return update_attendance_service(attendance_id, attendance_data)


@attendance_router.get(
    "/classes/{class_id}/attendance/",
    tags=["attendance"],
    response_model=List[AttendanceSchema],
    description="Get attendance records for a specific class"
)
def get_attendance_for_class(class_id: int):
    return get_attendance_for_class_service(class_id)