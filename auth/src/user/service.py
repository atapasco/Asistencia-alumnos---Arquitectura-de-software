from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from cryptography.fernet import Fernet
from config.bd import conn
from models.user import users

# Clave para la encriptación/desencriptación de contraseñas
key = Fernet.generate_key()
f = Fernet(key)

def create_user(user):
    try:
        # Preparar los datos del nuevo usuario
        new_user = {"email": user.email, "role": user.role}
        # Encriptar la contraseña
        new_user["password"] = f.encrypt(user.password.encode("utf-8"))
        
        # Insertar en la base de datos
        result = conn.execute(users.insert().values(new_user))
        
        # Devolver el usuario recién creado
        return conn.execute(users.select().where(users.c.email == result.lastrowid)).first()
    except SQLAlchemyError as e:
        print(f"Error creating user: {str(e)}")
        return None

def get_all_users():
    try:
        # Obtener todos los usuarios de la base de datos
        return conn.execute(users.select()).fetchall()
    except SQLAlchemyError as e:
        print(f"Error fetching users: {str(e)}")
        return None

def authenticate_user(email: str, password: str):
    try:
        # Buscar el usuario por su email
        user = conn.execute(users.select().where(users.c.email == email)).first()
        if user:
            # Comparar la contraseña desencriptada con la contraseña ingresada
            stored_password = f.decrypt(user.password.encode("utf-8")).decode("utf-8")
            if stored_password == password:
                # Construir un diccionario manualmente
                user_dict = {
                    "password": user.password,
                    "email": user.email,
                    "role": user.role
                }
                return user_dict
        return None  # Credenciales inválidas
    except SQLAlchemyError as e:
        print(f"Error during authentication: {str(e)}")
        return None