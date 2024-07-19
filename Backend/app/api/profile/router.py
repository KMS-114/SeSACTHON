from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from .schema import ProfileCollection, ProfileModel
from .repository import get_profiles, create_profile_document
from .service import refactoring_profile, refactoring_profile_test, create_profile_test

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

@router.get("/create")
async def profile_create_singleaudio(userId: str, file: UploadFile = File(...)):
    try:
        generate_profile = refactoring_profile(userId, file)
        return generate_profile
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.post("/save", response_model=ProfileModel, response_model_by_alias=False)
async def profile_save(profile: ProfileModel):
    print(profile)
    try:
        result = await create_profile_document(profile)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/create_test")
async def profile_create_test(userId: str):
    try:
        result = await refactoring_profile_test(userId)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/save_test")
async def profile_create_test(profile: ProfileModel):
    try:
        result = await create_profile_test(profile)
        return JSONResponse(content={"message": "Success", "data": result})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))