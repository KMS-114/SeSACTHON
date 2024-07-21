from fastapi import APIRouter, UploadFile, File, HTTPException, Form

from .schema import ResumeModel, ResumeCollection
from .repository import get, create, get_all, delete, update
from .service import generate_resume
from fastapi.responses import JSONResponse, FileResponse
from typing import List

import subprocess
import shutil
from pathlib import Path
from typing import List


router = APIRouter(prefix="/resume")


@router.get(
    "/all",
    response_model=ResumeCollection,
    response_model_by_alias=False,
)
async def list_resumes():
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

        # ffmpeg command to convert webm to mp3
        ffmpeg_path = "D:\\ffmpeg-7.0.1-essentials_build\\bin\\ffmpeg.exe"  # Update this path if ffmpeg is not in the system PATH
        command = [ffmpeg_path, "-y", "-i", str(input_file_path), str(output_file_path)]
        subprocess.run(command, check=True)

        return FileResponse(output_file_path, media_type="audio/mpeg", filename=output_file_path.name)
    except Exception as e:
        return JSONResponse(content={"message": str(e)}, status_code=500)

@router.post("/create", response_model=ResumeModel, response_model_by_alias=False)
async def resume_create(resume: ResumeModel):
    result = await create(resume=resume)

    if result is None:
        raise HTTPException(status_code=409, detail="Resume already exists for the given username and jobPostingId.")

    return result

@router.post("/generate")
async def resume_generate(username: str = Form(...), question: List[str] = Form(...), file: UploadFile = File(...)):
    try:
        generate_answer = await generate_resume(username=username, question=question, file=file)
        return generate_answer
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.put("/update", response_model=ResumeModel, response_model_by_alias=False)
async def resume_update(resume: ResumeModel):
    try:
        result = await update(resume=resume)
        if result is None:
            raise HTTPException(status_code=404, detail="Profile not found")
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/get")
async def resume_get(username: str, jobPostingId: str):
    try:
        return await get(username=username, jobPostingId=jobPostingId)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/delete")
async def resume_delete(username: str, jobPostingId: str):
    try:
        result_message = await delete(username=username, jobPostingId=jobPostingId)
        if result_message == 'Document successfully deleted.':
            return {"detail": result_message}
        else:
            raise HTTPException(status_code=404, detail=result_message)
    except Exception as e:
        if "Database error" in str(e):
            raise HTTPException(status_code=500, detail="Internal server error occurred")
        else:
            raise HTTPException(status_code=500, detail="Unexpected error occurred")


@router.post("/generate_test")
async def resume_generate_test(username: str, question: List[str], answer: str):
    try:
        generate_answer = await generate_resume_test(username=username, question=question, answer=answer)
        return generate_answer
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))