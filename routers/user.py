# routes/user.py
from fastapi import APIRouter, HTTPException
from schemas.user import User
from typing import List
from service.user_service import create_user, get_all_users, authenticate_user

user = APIRouter()

@user.get("/users", tags=["users"], response_model=List[User], description="Get a list of all users")
def get_users():
    return get_all_users()

@user.post("/user_post", tags=["users"], response_model=User, description="Create a new user")
def create_user_endpoint(user: User):
    return create_user(user)

# Nuevo endpoint para iniciar sesión
@user.post("/login", tags=["users"], description="Authenticate a user")
def login(email: str, password: str):
    authenticated_user = authenticate_user(email, password)
    if authenticated_user:
        return {"message": "Login successful", "user": authenticated_user}
    else:
        raise HTTPException(status_code=401, detail="Invalid email or password")