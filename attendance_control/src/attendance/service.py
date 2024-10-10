from sqlalchemy import insert, update, select
from database import conn
from .models import attendance  
from fastapi import HTTPException
from .schemas import AttendanceSchema
from notifications.service import start_timer, cancel_timer

def register_attendance_service(class_id: int, attendance_data: AttendanceSchema, correo: str):
    try:
        new_attendance = {
            "student_id": attendance_data.student_id,
            "class_id": class_id,
            "date": attendance_data.date,
            "status": attendance_data.status,
        }

        if attendance_data.status == "Ausente":
            start_timer(correo)

        result = conn.execute(attendance.insert().values(new_attendance))
        created_attendance = conn.execute(attendance.select().where(attendance.c.id == result.lastrowid)).first()

        if not created_attendance:
            raise HTTPException(status_code=500, detail="Attendance registration failed")

        return created_attendance

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error registering attendance: {str(e)}")


def update_attendance_service(attendance_id: int, attendance_data: AttendanceSchema, correo: str):
    try:
        query = attendance.update().where(attendance.c.id == attendance_id).values(
            student_id=attendance_data.student_id,
            class_id=attendance_data.class_id,
            date=attendance_data.date,
            status=attendance_data.status,
        )
        if attendance_data.status == "Ausente":
            start_timer(correo)
        if attendance_data.status == "Presente":
            cancel_timer(correo)

        result = conn.execute(query)
        
        if result.rowcount == 0:
            raise HTTPException(status_code=404, detail="Attendance record not found")
        
        updated_attendance = conn.execute(attendance.select().where(attendance.c.id == attendance_id)).first()
        
        return updated_attendance

    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error updating attendance: {str(e)}")


def get_attendance_for_class_service(class_id: int):
    try:
        query = attendance.select().where(attendance.c.class_id == class_id)
        result = conn.execute(query).fetchall()

        if not result:
            raise HTTPException(status_code=404, detail="No attendance records found for this class")

        return result

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching attendance records: {str(e)}")