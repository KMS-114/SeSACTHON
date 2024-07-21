from datetime import datetime
from fastapi import APIRouter

from .schema import UserModel, UserCollection
from .repository import find_all_users, create_user, delete_user, find_user


router = APIRouter(prefix="/user")


@router.post("/create", response_model=UserModel, response_model_by_alias=False)
async def user_create(user: UserModel):
    return await create_user(user=user)


@router.get("/all", response_model=UserCollection, response_model_by_alias=False)
async def list_users():
    return await find_all_users()


@router.get("/get/{username}", response_model=UserModel, response_model_by_alias=False)
async def user_get(username: str):
    return await find_user(username=username)


@router.get("/drop/{username}", response_model=UserModel, response_model_by_alias=False)
async def user_delete(username: str):
    return await delete_user(username=username)
