from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse, FileResponse
from typing import Optional
from .schema import ProfileCollection, ProfileModel
from .repository import get_profiles, create_profile_document
from .service import refactoring_profile_with_mp3, refactoring_profile_with_text, refactoring_profile_test, create_profile_test

import subprocess
import shutil
from pathlib import Path


router = APIRouter(prefix="/profile")

TEMP_DIR = Path("temp")
TEMP_DIR.mkdir(parents=True, exist_ok=True)

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

@router.post("/get_webm")
async def convert_and_upload(file: UploadFile = File(...)):
    try:
        input_file_path = TEMP_DIR / file.filename
        output_file_path = input_file_path.with_suffix(".mp3")

        with open(input_file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # ffmpeg command to convert webm to mp3
        ffmpeg_path = "D:\\ffmpeg-7.0.1-essentials_build\\bin\\ffmpeg.exe"  # Update this path if ffmpeg is not in the system PATH
        command = [ffmpeg_path, "-i", str(input_file_path), str(output_file_path)]
        subprocess.run(command, check=True)

        return FileResponse(output_file_path, media_type="audio/mpeg", filename=output_file_path.name)
    except Exception as e:
        return JSONResponse(content={"message": str(e)}, status_code=500)


@router.post("/send_mp3")
async def profile_create_singeaudio(username: str, file: UploadFile = File(...)):
    try:
        generate_profile = await refactoring_profile_with_mp3(username, file)
        return generate_profile
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
    
@router.post("/send_text")
async def profile_create_singletext(username: str, content: str):
    try:
        generate_profile = await refactoring_profile_with_text(username, content)
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