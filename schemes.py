from pydantic import BaseModel, EmailStr
from typing import Optional

class User(BaseModel):
    name: str
    lastname: str
    email: str
    password: str
    status: Optional[int] = None

class UserGet(BaseModel):
    name: str
    lastname: str
    email: str
    status: int

    class Config:
        orm_mode = True
