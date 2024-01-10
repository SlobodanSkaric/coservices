from sqlalchemy.orm import Session
from db import get_db
from passlib.context import CryptContext
from fastapi import Response, Depends, HTTPException, APIRouter
from db_models.user_model import User
import schemes
router = APIRouter(prefix="/user", tags=["Users"])


pass_context = CryptContext(schemes=["bcrypt"], deprecated="auto")



@router.post("/create",response_model=schemes.UserGet)
async def create_user(user: schemes.User, db: Session = Depends(get_db)):
    password = user.password
    password_hash = pass_context.hash(password)
    user.password = password_hash
    user_add = User(**user.model_dump())

    db.add(user_add)
    db.commit()
    db.flush(user_add)

    return user_add
