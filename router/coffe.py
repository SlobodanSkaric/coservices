from fastapi import Depends, HTTPException, status, APIRouter
from sqlalchemy.orm import Session
from db import get_db
import auth
import schemes
from db_models.user_model import Coffes,User

router = APIRouter(prefix="/coffe", tags=["Coffes"])


@router.post("/create/{id}", response_model=schemes.Coffe)
async def create_coffe(id: int,coffe_data: schemes.Coffe, db: Session = Depends(get_db), curent_user: dict = Depends(auth.auth_token)):
    coffe_checked_query = db.query(Coffes).filter(Coffes.coffe_name == coffe_data.coffe_name).first()
    #implemnet user checker and add data in user coffe tabele
    user_check_query = db.query(User).filter(User.user_id == id).first()

    if not user_check_query:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="This user is not register")

    if id != curent_user.user_id:
        raise  HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not valid premmision")
    #add role
    if coffe_checked_query:
        raise HTTPException(status_code=status.HTTP_306_RESERVED, detail="Coffe with this name is existe")

    coffe = coffe_data.model_dump()
    coffe_add = Coffes(**coffe)

    db.add(coffe_add)
    db.commit()
    db.refresh(coffe_add)

    return coffe_add
