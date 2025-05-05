from fastapi import APIRouter
from app.users.models.user import UserV2
from app.users.services import service


router = APIRouter(prefix="/api/v2", tags=["Users v2"])

@router.get("/users", response_model=list[UserV2])
async def get_users():
    return await service.get_users_v2()

@router.get("/users/{user_id}", response_model=UserV2)
async def get_user(user_id: int):
    return await service.get_user_v2(user_id)