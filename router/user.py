from sqlalchemy.orm import Session
from db import get_db
from passlib.context import CryptContext
from fastapi import Response, Depends, HTTPException, APIRouter, status
from db_models.user_model import User
import schemes
import auth

router = APIRouter(prefix="/user", tags=["Users"])

pass_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.post("/login")
async def user_login(user_data: schemes.UserLogin, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == user_data.email).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="This user is not existe")

    if not pass_context.verify(user_data.password, user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Password is not corect")

    create_token = auth.create_token({"user_id": user.user_id, "email": user.email})

    return create_token


@router.post("/create", response_model=schemes.UserGet)
async def create_user(user: schemes.User, db: Session = Depends(get_db)):
    password = user.password
    password_hash = pass_context.hash(password)
    user.password = password_hash
    user_add = User(**user.model_dump())

    db.add(user_add)
    db.commit()
    db.flush(user_add)

    return user_add

@router.get("/{id}", response_model=schemes.UserGet)
def get_user(id: int, db: Session = Depends(get_db), curent_user: dict = Depends(auth.auth_token)):
    if curent_user.user_id != id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Is not valid token")
    user = db.query(User).filter(User.user_id == id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    return user
