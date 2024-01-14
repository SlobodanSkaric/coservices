from fastapi import Depends, HTTPException, status, APIRouter
from sqlalchemy.orm import Session
from db import get_db
import auth
import schemes
from db_models.user_model import Coffes

router = APIRouter(prefix="/coffe", tags=["Coffes"])


@router.post("/create", response_model=schemes.Coffe)
async def create_coffe(coffe_data: schemes.Coffe, db: Session = Depends(get_db)):
    coffe_checked_query = db.query(Coffes).filter(Coffes.coffe_name == coffe_data.coffe_name).first()
    #implemnet user checker and add data in user coffe tabele
    #add time expirien token
    #add role
    if coffe_checked_query:
        raise HTTPException(status_code=status.HTTP_306_RESERVED, detail="Coffe with this name is existe")

    coffe = coffe_data.model_dump()
    coffe_add = Coffes(**coffe)

    db.add(coffe_add)
    db.commit()
    db.refresh(coffe_add)

    return coffe_add
