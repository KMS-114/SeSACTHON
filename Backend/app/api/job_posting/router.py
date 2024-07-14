from fastapi import APIRouter

from .schema import JobPostingModel, JobPostingCollection
from .repository import find_all_job_postings


router = APIRouter(prefix="/job_posting")


# async def create_job_posting():


@router.get("/all", response_model=JobPostingCollection, response_model_by_alias=False)
async def list_job_postings():
    return await find_all_job_postings()
