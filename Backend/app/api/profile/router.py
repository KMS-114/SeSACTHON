from fastapi import APIRouter

from api.profile.schema import ProfileCollection, ProfileModel
from api.profile.repository import get_profiles, create_profile


router = APIRouter(prefix="/profile")


@router.get(
    "/all",
    response_model=ProfileCollection,
    response_model_by_alias=False,
)
async def list_profiles():
    return await get_profiles()


@router.post("/create", response_model=ProfileModel, response_model_by_alias=False)
async def profile_create(profile: ProfileModel):
    return await create_profile(profile)
