from fastapi import APIRouter

from .schema import JobPostingModel, JobPostingCollection, CoverLetterQuestion, QualificationRequired
from .repository import get_job_postings, create_job_posting, update_cover_letter_question, update_qualification, update_description
from ...database import collection
from bson import ObjectId

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

@router.get(
    "/all",
    response_model = JobPostingCollection,
    response_model_by_alias=False
)
async def list_job_postings():
    return await get_job_postings()