from config.bd import conn
from models.professor import professors
from schemas.professor import ProfessorSchema
from sqlalchemy.exc import SQLAlchemyError

def get_all_professors():
    try:
        # Consulta a la base de datos para obtener todos los profesores
        result = conn.execute(professors.select()).fetchall()
        return result
    except SQLAlchemyError as e:
        print(f"Error al obtener profesores: {e}")
        return []

def create_new_professor(professor: ProfessorSchema):
    try:
        # Inserta un nuevo profesor en la base de datos
        new_professor = {
            "id": professor.id,
            "user_email": professor.user_email,
            "name": professor.name,
            "birth_date": professor.birth_date,
        }
        result = conn.execute(professors.insert().values(new_professor))
        return conn.execute(professors.select().where(professors.c.id == result.lastrowid)).first()
    except SQLAlchemyError as e:
        print(f"Error al crear nuevo profesor: {e}")
        return None

def get_professor_by_id(id: str):
    try:
        # Obtiene un profesor específico por ID
        return conn.execute(professors.select().where(professors.c.id == id)).first()
    except SQLAlchemyError as e:
        print(f"Error al obtener profesor con ID {id}: {e}")
        return None

def delete_professor_by_id(id: str):
    try:
        result = conn.execute(professors.delete().where(professors.c.id == id))
        return result.rowcount > 0  # Retorna True si se eliminó algún registro
    except SQLAlchemyError as e:
        print(f"Error al eliminar profesor con ID {id}: {e}")
        return False