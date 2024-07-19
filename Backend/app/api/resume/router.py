from fastapi import APIRouter

from api.resume.schema import ResumeModel, ResumeCollection
from api.resume.repository import get_resumes, create_resume


router = APIRouter(prefix="/resume")


@router.get(
    "/all",
    response_model=ResumeCollection,
    response_model_by_alias=False,
)
async def list_resumes():
    return await get_resumes()


@router.post("/create", response_model=ResumeModel, response_model_by_alias=False)
async def resume_create(resume: ResumeModel):
    return await create_resume(resume)
