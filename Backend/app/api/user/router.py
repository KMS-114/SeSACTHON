from fastapi import APIRouter

from .schema import UserModel, UserCollection
from .repository import get_users


router = APIRouter(prefix="/user")


@router.get(
    "/all",
    response_model=UserCollection,
    response_model_by_alias=False
)
async def list_users():
    return await get_users()
