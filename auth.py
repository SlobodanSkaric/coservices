from jose import jwt,JWTError
from datetime import datetime,timedelta

SECRET_KEY = "a6b46dd0d1ae5e86cbc8f37e75ceeb6760230c1ca4ffbcb0c97b96dd7d9c464b"
ALGORITHM = "HS256"
EXPIRIES = 30

def create_token(data: dict):
    prepare_data = data.copy()

    expirie_time = datetime.utcnow() + timedelta(minutes=EXPIRIES)
    prepare_data.update({"exp": expirie_time})

    jwt_token = jwt.encode(prepare_data,SECRET_KEY,ALGORITHM)

    return jwt_token