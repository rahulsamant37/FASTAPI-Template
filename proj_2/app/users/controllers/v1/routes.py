from fastapi import APIRouter
from app.users.models.user import UserV1
from app.users.services import service

router = APIRouter(prefix="/api/v1", tags=["Users v1"])

@router.get("/users", response_model=list[UserV1])
async def get_users():
    return await service.get_users_v1()

@router.get("/users/{user_id}", response_model=UserV1)
async def get_user(user_id: int):
    return await service.get_user_v1(user_id)