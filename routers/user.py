from fastapi import APIRouter
from config.bd import conn
from models.user import users
from schemas.user import User, UserCount
from typing import List
from starlette.status import HTTP_204_NO_CONTENT
from sqlalchemy import func, select

from cryptography.fernet import Fernet

user = APIRouter()
key = Fernet.generate_key()
f = Fernet(key)


@user.get(
    "/users",
    tags=["users"],
    response_model=List[User],
    description="Get a list of all users",
)
def get_users():
    return conn.execute(users.select()).fetchall()

@user.post("/", tags=["users"], response_model=User, description="Create a new user")
def create_user(user: User):
    new_user = {"email": user.email, "role":user.role}
    new_user["password"] = f.encrypt(user.password.encode("utf-8"))
    result = conn.execute(users.insert().values(new_user))
    return conn.execute(users.select().where(users.c.email == result.lastrowid)).first()