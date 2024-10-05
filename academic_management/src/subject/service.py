from config.bd import conn
from .models import subjects
from .schemas import SubjectSchema
from sqlalchemy.exc import SQLAlchemyError

def get_all_subjects():
    try:
        return conn.execute(subjects.select()).fetchall()
    except SQLAlchemyError as e:
        print(f"Error fetching subjects: {str(e)}")
        return []

def create_new_subject(subject: SubjectSchema):
    try:
        new_subject = {
            "name": subject.name,
            "description": subject.description,
        }
        result = conn.execute(subjects.insert().values(new_subject))
        return conn.execute(subjects.select().where(subjects.c.id == result.lastrowid)).first()
    except SQLAlchemyError as e:
        print(f"Error creating subject: {str(e)}")
        return None