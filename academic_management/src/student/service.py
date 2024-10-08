from database import conn
from .models import students
from .schemas import StudentSchema
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError

def get_all_students():
    try:

        result = conn.execute(select(students)).fetchall()
        return result
    except SQLAlchemyError as e:
        print(f"Error al obtener estudiantes: {e}")
        return []

def create_new_student(student: StudentSchema):
    try:
        
        new_student = {
            "user_email": student.user_email,
            "name": student.name,
            "birth_date": student.birth_date,
            "grade": student.grade,
        }
      
        result = conn.execute(students.insert().values(new_student))
        
        return conn.execute(select(students).where(students.c.id == result.lastrowid)).mappings().first()
    except SQLAlchemyError as e:
      
        print(f"Error al crear nuevo estudiante: {e}")
        return None