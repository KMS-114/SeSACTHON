from fastapi import APIRouter

from .schema import ResumeModel, ResumeCollection
from .repository import get_resumes


router = APIRouter(prefix="/resume")


@router.get(
    "/all",
    response_model=ResumeCollection,
    response_model_by_alias=False,
)
async def list_resumes():
    return await get_resumes()