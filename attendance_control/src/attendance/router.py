from fastapi import APIRouter, HTTPException
from database import conn
from .models import attendance  # Modelo de la tabla 'attendance'
from .schemas import AttendanceSchema  # Asegúrate de que esta ruta sea correcta
from fastapi.encoders import jsonable_encoder
from typing import List

attendance_router = APIRouter()

# Endpoint para registrar la asistencia de un alumno
@attendance_router.post(
    "/classes/{class_id}/attendance/",
    tags=["attendance"],
    response_model=AttendanceSchema,
    description="Register attendance for a specific class"
)
def register_attendance(class_id: int, attendance_data: AttendanceSchema):
    new_attendance = {
        "student_id": attendance_data.student_id,
        "class_id": class_id,
        "date": attendance_data.date,
        "status": attendance_data.status,
    }

    result = conn.execute(attendance.insert().values(new_attendance))
    created_attendance = conn.execute(attendance.select().where(attendance.c.id == result.lastrowid)).first()
    
    if not created_attendance:
        raise HTTPException(status_code=500, detail="Attendance registration failed")
    
    return created_attendance

# Endpoint para modificar la asistencia de un alumno
@attendance_router.put(
    "/attendance/{attendance_id}",
    tags=["attendance"],
    response_model=AttendanceSchema,
    description="Update attendance record"
)

def update_attendance(attendance_id: int, attendance_data: AttendanceSchema):
    query = attendance.update().where(attendance.c.id == attendance_id).values(
        student_id=attendance_data.student_id,
        class_id=attendance_data.class_id,
        date=attendance_data.date,
        status=attendance_data.status,
    )
    
    result = conn.execute(query)
    
    if result.rowcount == 0:
        raise HTTPException(status_code=404, detail="Attendance record not found")
    
    updated_attendance = conn.execute(attendance.select().where(attendance.c.id == attendance_id)).first()
    
    return updated_attendance

# Endpoint para consultar la asistencia de una clase específica
@attendance_router.get(
    "/classes/{class_id}/attendance/",
    tags=["attendance"],
    response_model=List[AttendanceSchema],
    description="Get attendance records for a specific class"
)
def get_attendance_for_class(class_id: int):
    query = attendance.select().where(attendance.c.class_id == class_id)
    result = conn.execute(query).fetchall()
    
    if not result:
        raise HTTPException(status_code=404, detail="No attendance records found for this class")
    
    return result