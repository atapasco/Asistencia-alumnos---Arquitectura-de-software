from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from .models import classes
from .schemas import ClassCreate, ClassResponse
from database import SessionLocal  # Asegúrate de importar tu SessionLocal


def create_class(class_data: ClassCreate):
    try:
        with SessionLocal() as session:
            new_class = {
                "name": class_data.name,
                "professor_id": class_data.professor_id,
                "subject_id": class_data.subject_id,
            }
            result = session.execute(classes.insert().values(new_class))
            session.commit()

            return (
                session.execute(
                    select(classes).where(classes.c.id == result.lastrowid)
                )
                .mappings()
                .first()
            )
    except SQLAlchemyError as e:
        print(f"Error creating class: {str(e)}")
        raise


def get_all_classes():
    try:
        with SessionLocal() as session:

            return session.execute(classes.select()).fetchall()
    except SQLAlchemyError as e:
        print(f"Error fetching classes: {str(e)}")
        raise


def get_class_by_id(class_id: int):
    try:
        with SessionLocal() as session:
            class_ = session.execute(
                select(classes).where(classes.c.id == class_id)
            ).scalar_one_or_none()
            if class_:
                return ClassResponse.from_orm(class_)
            return None
    except SQLAlchemyError as e:
        print(f"Error fetching class by id: {str(e)}")
        raise


def update_class(class_id: int, class_data: ClassCreate):
    try:
        with SessionLocal() as session:
            update_data = {}
            if class_data.name:
                update_data["name"] = class_data.name
            if class_data.professor_id:
                update_data["professor_id"] = class_data.professor_id
            if class_data.subject_id:
                update_data["subject_id"] = class_data.subject_id

            result = session.execute(
                classes.update().where(classes.c.id == class_id).values(**update_data)
            )
            session.commit()

            if result.rowcount == 0:
                return None

            return get_class_by_id(class_id)  #
    except SQLAlchemyError as e:
        print(f"Error updating class: {str(e)}")
        raise


def delete_class(class_id: int):
    try:
        with SessionLocal() as session:
            result = session.execute(classes.delete().where(classes.c.id == class_id))
            session.commit()
            return result.rowcount > 0
    except SQLAlchemyError as e:
        print(f"Error deleting class: {str(e)}")
        raise
