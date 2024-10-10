# routes/user.py
from fastapi import APIRouter, HTTPException,Body
from .schemas import User,UserLogin
from typing import List
from .service import create_user, get_all_users, authenticate_user

user = APIRouter()

@user.get("/users", tags=["users"], response_model=List[User], description="Get a list of all users")
def get_users():
    return get_all_users()

@user.post("/user_post", tags=["users"], response_model=User, description="Create a new user")
def create_user_endpoint(user: User):
    return create_user(user)

# Nuevo endpoint para iniciar sesión
@user.post("/login", tags=["users"], description="Authenticate a user")
def login(login_data: UserLogin = Body(...)):
    authenticated_user = authenticate_user(login_data.email, login_data.password)
    if authenticated_user:
        return {"message": "Login successful", "user": authenticated_user}
    else:
        raise HTTPException(status_code=401, detail="Invalid email or password")