from database import conn
from .models import subjects
from .schemas import SubjectSchema
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker
from database import engine

SessionLocal = sessionmaker(bind=engine)


def get_all_subjects():
    try:
        with SessionLocal() as session:
            return session.execute(subjects.select()).fetchall()
    except SQLAlchemyError as e:
        print(f"Error fetching subjects: {str(e)}")
        return []


def create_new_subject(subject: SubjectSchema):
    try:
        with SessionLocal() as session:
            new_subject = {
                "name": subject.name,
                "description": subject.description,
            }
            result = session.execute(subjects.insert().values(new_subject))
            session.commit()
            return session.execute(
                subjects.select().where(subjects.c.id == result.lastrowid)
            ).first()
    except SQLAlchemyError as e:
        print(f"Error creating subject: {str(e)}")
        return None
