from fastapi import APIRouter

from .schema import ProfileCollection, ProfileModel
from .repository import get_profiles


router = APIRouter(prefix="/profile")


@router.get(
    "/all",
    response_model=ProfileCollection,
    response_model_by_alias=False,
)
async def list_profiles():
    return await get_profiles()