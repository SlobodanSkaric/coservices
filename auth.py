from jose import jwt,JWTError
from datetime import datetime,timedelta
from db import get_db
from fastapi import Depends,HTTPException,status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from db_models.user_model import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

SECRET_KEY = "a6b46dd0d1ae5e86cbc8f37e75ceeb6760230c1ca4ffbcb0c97b96dd7d9c464b"
ALGORITHM = "HS256"
EXPIRIES = 30

def create_token(data: dict):
    prepare_data = data.copy()

    expirie_time = datetime.utcnow() + timedelta(minutes=EXPIRIES)
    prepare_data.update({"exp": expirie_time})

    jwt_token = jwt.encode(prepare_data,SECRET_KEY,ALGORITHM)

    return jwt_token

def virify_token(token, credencial_exexcption):
    try:
        payload = jwt.decode(token, SECRET_KEY, ALGORITHM)

        customer_id : int | None = payload.get("user_id")

        if id is None:
            raise credencial_exexcption
    except JWTError:
        raise credencial_exexcption

    return customer_id
def auth_token(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credencial_exeception = HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorize")

    get_token_user = virify_token(token, credencial_exeception)

    user = db.query(User).filter(User.user_id == get_token_user).first()

    return user