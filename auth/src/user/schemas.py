from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
    email: str
    password: str
    role: int


class UserCount(BaseModel):
    total: int