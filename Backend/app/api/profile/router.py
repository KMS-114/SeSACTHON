from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from .schema import ProfileCollection, ProfileModel
from .repository import get_profiles, create_profile
from service import create_profile

router = APIRouter(prefix="/profile")


@router.get(
    "/all",
    response_model=ProfileCollection,
    response_model_by_alias=False,
)
async def list_profiles():
    return await get_profiles()


# @router.post("/create", response_model=ProfileModel, response_model_by_alias=False)
# async def profile_create(profile: ProfileModel):
#     return await create_profile(profile)

@router.post("/create")
async def profile_create_singleaudio(userId: str, file: UploadFile = File(...)):
    try:
        result = await create_profile(userId, file)
        return JSONResponse(content={"message": "Success", "data": result})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
