from fastapi import APIRouter

router = APIRouter(prefix="/home", tags=["HomePage"])

@router.get("")
async def get_home():
    return {"message": "Home Page"}