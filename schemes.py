from pydantic import BaseModel, EmailStr
from typing import Optional

#User
class User(BaseModel):
    name: str
    lastname: str
    email: str
    password: str
    status: Optional[int] = None


class UserGet(BaseModel):
    user_id: int
    name: str
    lastname: str
    email: str
    status: int

    class Config:
        orm_mode = True


class UserLogin(BaseModel):
    email: str
    password: str

    class Config:
        orm_mode = True


#Coffe

class Coffe(BaseModel):
    coffe_name: str
    coffe_addres: str
    coffe_phone_number: str
    coffe_email: str
    coffe_status: int

