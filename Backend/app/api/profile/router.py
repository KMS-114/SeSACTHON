from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from typing import Optional
from .schema import ProfileCollection, ProfileModel

from .repository import get_all, create, get, delete, update
from .service import generate_profile, refactoring_profile_test, create_profile_test

router = APIRouter(prefix="/profile")


@router.get(
    "/all",
    response_model=ProfileCollection,
    response_model_by_alias=False,
)
async def list_profiles():
    return await get_all()


# @router.post("/create", response_model=ProfileModel, response_model_by_alias=False)
# async def profile_create(profile: ProfileModel):
#     return await create_profile(profile)

@router.post("/generate")
async def profile_generate(username: str, file: UploadFile = File(...)):
    try:
        profile = generate_profile(username, file)
        return profile
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.post("/create", response_model=ProfileModel, response_model_by_alias=False)
async def profile_create(profile: ProfileModel):
    try:
        result = await create(profile)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put("/update", response_model=ProfileModel, response_model_by_alias=False)
async def profile_update(profile: ProfileModel):
    try:
        result = await update(profile)
        if result is None:
            raise HTTPException(status_code=404, detail="Profile not found")
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/get")
async def resume_get(username: str):
    try:
        return await get(username)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/delete")
async def resume_delete(username: str):
    try:
        result_message = await delete(username)
        if result_message == 'Profile successfully deleted.':
            return {"detail": result_message}
        else:
            raise HTTPException(status_code=404, detail=result_message)
    except Exception as e:
        if "Database error" in str(e):
            raise HTTPException(status_code=500, detail="Internal server error occurred")
        else:
            raise HTTPException(status_code=500, detail="Unexpected error occurred")






@router.get("/create_test")
async def profile_create_test(username: str):
    try:
        result = await refactoring_profile_test(username)
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