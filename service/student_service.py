from config.bd import conn
from models.student import students
from schemas.student import StudentSchema
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError

def get_all_students():
    try:
        # Consulta a la base de datos para obtener todos los estudiantes
        result = conn.execute(select(students)).fetchall()
        return result
    except SQLAlchemyError as e:
        # Manejo de errores de SQLAlchemy
        print(f"Error al obtener estudiantes: {e}")
        return []

def create_new_student(student: StudentSchema):
    try:
        # Inserta un nuevo estudiante en la base de datos
        new_student = {
            "user_email": student.user_email,
            "name": student.name,
            "birth_date": student.birth_date,
            "grade": student.grade,
        }
        # Inserción en la tabla y obtención del último id insertado
        result = conn.execute(students.insert().values(new_student))
        
        # Retorna el nuevo registro de estudiante creado
        return conn.execute(select(students).where(students.c.id == result.lastrowid)).mappings().first()
    except SQLAlchemyError as e:
        # Manejo de errores de SQLAlchemy
        print(f"Error al crear nuevo estudiante: {e}")
        return None