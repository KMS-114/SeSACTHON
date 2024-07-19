from datetime import datetime
from fastapi import APIRouter

from api.user.schema import UserModel, UserCollection
from api.user.repository import find_all_users, create_user, delete_user, find_user


router = APIRouter(prefix="/user")


@router.post("/create", response_model=UserModel, response_model_by_alias=False)
async def user_create(user: UserModel):
    return await create_user(user=user)


@router.get("/all", response_model=UserCollection, response_model_by_alias=False)
async def list_users():
    return await find_all_users()


@router.get("/get/{user_id}", response_model=UserModel, response_model_by_alias=False)
async def user_get(user_id: str):
    return await find_user(user_id=user_id)


@router.get("/drop/{user_id}", response_model=UserModel, response_model_by_alias=False)
async def user_delete(user_id: str):
    return await delete_user(user_id=user_id)
