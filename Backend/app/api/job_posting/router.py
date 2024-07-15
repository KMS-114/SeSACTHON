from fastapi import APIRouter

from .schema import JobPostingModel, JobPostingCollection
from .repository import find_all_job_postings, create_job_posting
from ..user.repository import find_user


router = APIRouter(prefix="/job_posting")


# async def create_job_posting():


@router.get("/all", response_model=JobPostingCollection, response_model_by_alias=False)
async def list_job_postings():
    return await find_all_job_postings()


@router.post("/create", response_model=JobPostingModel, response_model_by_alias=False)
async def job_posting_create(job_posting: JobPostingModel):
    user_id = job_posting.userId
    user = await find_user(user_id)
    user_group = user.userGroup
    if user_group == 2:
        # 작성자가 고용주인지 확인
        return await create_job_posting(job_posting)
