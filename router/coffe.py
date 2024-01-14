from fastapi import Depends, HTTPException, status, APIRouter
from sqlalchemy.orm import Session
from db import get_db
import auth
import schemes
from db_models.user_model import Coffes

router = APIRouter(prefix="/coffe", tags=["Coffes"])


@router.post("/create", response_model=schemes.Coffe)
async def create_coffe(coffe_data: schemes.Coffe, db: Session = Depends(get_db)):

    coffe = coffe_data.model_dump()
    coffe_add = Coffes(**coffe)

    db.add(coffe_add)
    db.commit()
    db.refresh(coffe_add)

    return coffe_add
