from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from cryptography.fernet import Fernet
from dataclasses import conn
from .models import users

key = Fernet.generate_key()
f = Fernet(key)

def create_user(user):
    try:
        new_user = {"email": user.email, "role": user.role}
        new_user["password"] = f.encrypt(user.password.encode("utf-8"))
        
        result = conn.execute(users.insert().values(new_user))
        
        return conn.execute(users.select().where(users.c.email == result.lastrowid)).first()
    except SQLAlchemyError as e:
        print(f"Error creating user: {str(e)}")
        return None

def get_all_users():
    try:
        
        return conn.execute(users.select()).fetchall()
    except SQLAlchemyError as e:
        print(f"Error fetching users: {str(e)}")
        return None

def authenticate_user(email: str, password: str):
    try:
        user = conn.execute(users.select().where(users.c.email == email)).first()
        if user:
            
            stored_password = f.decrypt(user.password.encode("utf-8")).decode("utf-8")
            if stored_password == password:
                
                user_dict = {
                    "password": user.password,
                    "email": user.email,
                    "role": user.role
                }
                return user_dict
        return None 
    except SQLAlchemyError as e:
        print(f"Error during authentication: {str(e)}")
        return None