from .models import professors
from .schemas import ProfessorSchema
from sqlalchemy.exc import SQLAlchemyError
from database import engine 
from sqlalchemy.orm import sessionmaker

SessionLocal = sessionmaker(bind=engine)



def get_all_professors():
    try:
        with SessionLocal() as session:
            result = session.execute(professors.select()).fetchall()
        return result
    except SQLAlchemyError as e:
        print(f"Error al obtener profesores: {e}")
        return []

def create_new_professor(professor: ProfessorSchema):
    try:
        with SessionLocal() as session:
            new_professor = {
                "id": professor.id,
                "user_email": professor.user_email,
                "name": professor.name,
                "birth_date": professor.birth_date,
            }
            result = session.execute(professors.insert().values(new_professor))
            session.commit()
            return session.execute(professors.select().where(professors.c.id == result.lastrowid)).first()
    except SQLAlchemyError as e:
        print(f"Error al crear nuevo profesor: {e}")
        return None

def get_professor_by_id(id: str):
    try:
        with SessionLocal() as session:
            return session.execute(professors.select().where(professors.c.id == id)).first()
    except SQLAlchemyError as e:
        print(f"Error al obtener profesor con ID {id}: {e}")
        return None

def delete_professor_by_id(id: str):
    try:
        with SessionLocal() as session:
            result = session.execute(professors.delete().where(professors.c.id == id))
            return result.rowcount > 0 
    except SQLAlchemyError as e:
        print(f"Error al eliminar profesor con ID {id}: {e}")
        return False