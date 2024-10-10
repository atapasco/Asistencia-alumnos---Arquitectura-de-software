from database import engine
from .models import students
from .schemas import StudentSchema
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker


SessionLocal = sessionmaker(bind=engine)


def get_all_students():
    try:
        with SessionLocal() as session:
            result = session.execute(select(students)).fetchall()
            return result
    except SQLAlchemyError as e:
        print(f"Error al obtener estudiantes: {e}")
        return []


def create_new_student(student: StudentSchema):
    try:
        with SessionLocal() as session:
            new_student = {
                "user_email": student.user_email,
                "name": student.name,
                "birth_date": student.birth_date,
                "grade": student.grade,
            }

            result = session.execute(students.insert().values(new_student))
            session.commit()

            return (
                session.execute(
                    select(students).where(students.c.id == result.lastrowid)
                )
                .mappings()
                .first()
            )
    except SQLAlchemyError as e:

        print(f"Error al crear nuevo estudiante: {e}")
        return None
