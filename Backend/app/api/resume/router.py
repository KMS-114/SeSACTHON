from fastapi import APIRouter, UploadFile, File, HTTPException

from .schema import ResumeModel, ResumeCollection
from .repository import get, create, get_all, delete, update
from .service import generate_resume

router = APIRouter(prefix="/resume")


@router.get(
    "/all",
    response_model=ResumeCollection,
    response_model_by_alias=False,
)
async def list_resumes():
    return await get_all()


@router.post("/create", response_model=ResumeModel, response_model_by_alias=False)
async def resume_create(resume: ResumeModel):
    result = await create(resume)

    if result is None:
        raise HTTPException(status_code=409, detail="Resume already exists for the given username and jobPostingId.")

    return result
@router.post("/generate")
async def resume_generate(username: str, question: list[str], file: UploadFile = File(...)):
    try:
        generate_answer = generate_resume(username, question, file)
        return generate_answer
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.put("/update", response_model=ResumeModel, response_model_by_alias=False)
async def resume_update(resume: ResumeModel):
    try:
        result = await update(resume)
        if result is None:
            raise HTTPException(status_code=404, detail="Profile not found")
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/get")
async def resume_get(username: str, jobPostingId: str):
    try:
        return await get(username, jobPostingId)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/delete")
async def resume_delete(username: str, jobPostingId: str):
    try:
        result_message = await delete(username, jobPostingId)
        if result_message == 'Document successfully deleted.':
            return {"detail": result_message}
        else:
            raise HTTPException(status_code=404, detail=result_message)
    except Exception as e:
        if "Database error" in str(e):
            raise HTTPException(status_code=500, detail="Internal server error occurred")
        else:
            raise HTTPException(status_code=500, detail="Unexpected error occurred")