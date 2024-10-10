from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
    email: str
    password: str
    role: int

class UserLogin(BaseModel):
    email: str
    password: str

class UserCount(BaseModel):
    total: int