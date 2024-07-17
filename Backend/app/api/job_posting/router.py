from fastapi import APIRouter

from .schema import JobPostingModel, JobPostingCollection, CoverLetterQuestion, QualificationRequired
from .repository import find_all_job_postings, create_job_posting, update_cover_letter_question, update_qualification, update_description
from ...database import collection
from bson import ObjectId
from ..user.repository import find_user


router = APIRouter(prefix="/job_posting")

@router.put("/description")
async def api_description(job_posting_id:str, description:str):
    return await update_description(job_posting_id, description)

@router.put("/cover_letter_question/")
async def api_cover_letter_question(job_posting_id:str, content:str, char_limit:int):
    return await update_cover_letter_question(job_posting_id, content, char_limit)
    
@router.put("/qualification/")
async def api_update_qualification(job_posting_id:str, key:str, value:str):
    return await update_qualification(job_posting_id, key, value)

@router.post("/jop_posting")
async def api_job_posting(job_posting:JobPostingModel):
    job_posting_dict = await create_job_posting(job_posting)
    return {"message": "jobposting created successfully"}

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
