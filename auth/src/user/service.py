from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from passlib.context import CryptContext
from .models import users
from database import engine  # Asegúrate de importar tu engine

# Crear el contexto para las contraseñas
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Crear una sesión local
SessionLocal = sessionmaker(bind=engine)

def create_user(user):
    try:
        # Usar el contexto de la sesión
        with SessionLocal() as session:
            new_user = {
                "email": user.email,
                "role": user.role,
                "password": pwd_context.hash(user.password)
            }
            
            session.execute(users.insert().values(new_user))
            session.commit()
            
            return session.execute(users.select().where(users.c.email == user.email)).first()
    except SQLAlchemyError as e:
        print(f"Error creating user: {str(e)}")
        raise  # Re-lanzar la excepción para manejo superior

def get_all_users():
    try:
        with SessionLocal() as session:
            return session.execute(users.select()).fetchall()
    except SQLAlchemyError as e:
        print(f"Error fetching users: {str(e)}")
        raise

def authenticate_user(email: str, password: str):
    try:
        with SessionLocal() as session:
            # Busca el usuario por su email en la base de datos
            user = session.execute(users.select().where(users.c.email == email)).first()
            
            # Si el usuario no existe, retorna None
            if user is None:
                return None
            
            # El hash de la contraseña almacenada está en user.password
            stored_password_hash = user.password
            
            # Verificar si la contraseña ingresada es correcta
            if pwd_context.verify(password, stored_password_hash):
                # Si la contraseña es correcta, retorna el usuario
                return {
                    "email": user.email,
                    "role": user.role
                }
            else:
                # Si la contraseña es incorrecta, retorna None
                return None
    except SQLAlchemyError as e:
        print(f"Error during authentication: {str(e)}")
        raise