from fastapi import APIRouter, UploadFile, File, HTTPException, Form
from fastapi.responses import JSONResponse, FileResponse
from .schema import ProfileCollection, ProfileModel

from .repository import get_all, create, get, delete, update
from .service import generate_profile, refactoring_profile_test, create_profile_test

import subprocess
import shutil
from pathlib import Path

router = APIRouter(prefix="/profile")


@router.get(
    "/all",
    response_model=ProfileCollection,
    response_model_by_alias=False,
)
async def list_profiles():
    return await get_all()

@router.post("/get_webm")
async def convert_and_upload(username: str = Form(...), type: str = Form(...), file: UploadFile = File(...)):
    try:
        TEMP_DIR = Path(f"data/{type}/{username}")
        TEMP_DIR.mkdir(parents=True, exist_ok=True)
        input_file_path = TEMP_DIR / file.filename
        output_file_path = input_file_path.with_suffix(".wav")

        with open(input_file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # ffmpeg 파일 설치 경로 설정
        ffmpeg_path = "D:\\ffmpeg-7.0.1-essentials_build\\bin\\ffmpeg.exe"  # Update this path if ffmpeg is not in the system PATH
        command = [ffmpeg_path, "-y", "-i", str(input_file_path), str(output_file_path)]
        subprocess.run(command, check=True)

        return FileResponse(output_file_path, media_type="audio/mpeg", filename=output_file_path.name)
    except Exception as e:
        return JSONResponse(content={"message": str(e)}, status_code=500)


# @router.post("/create", response_model=ProfileModel, response_model_by_alias=False)
# async def profile_create(profile: ProfileModel):
#     return await create_profile(profile)

@router.post("/generate")
async def profile_generate(username: str = Form(...), file: UploadFile = File(...)):
    try:
        profile = await generate_profile(username=username, file=file)
        return profile
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.post("/create", response_model=ProfileModel, response_model_by_alias=False)
async def profile_create(profile: ProfileModel):
    try:
        result = await create(profile=profile)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put("/update", response_model=ProfileModel, response_model_by_alias=False)
async def profile_update(profile: ProfileModel):
    try:
        result = await update(profile=profile)
        if result is None:
            raise HTTPException(status_code=404, detail="Profile not found")
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/get")
async def resume_get(username: str):
    try:
        return await get(username=username)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/delete")
async def resume_delete(username: str):
    try:
        result_message = await delete(username=username)
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