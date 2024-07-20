from bson.objectid import ObjectId

from ...database import mongodb
from .schema import ResumeModel, ResumeCollection

from ..job_posting.schema import JobPostingModel

collection = mongodb.get_collection("resume")

async def create_resume(resume: ResumeModel) -> ResumeModel:
    collection_job = mongodb.get_collection("jobPosting")
    job_posting = await collection_job.find_one({"_id": ObjectId(resume.jobPostingId)})
    job_posting = JobPostingModel(**job_posting)

    new_resume = await collection.insert_one(
        resume.model_dump(by_alias=True, exclude=["id"])
    )
    created_resume = await collection.find_one({"_id": new_resume.inserted_id})
    return created_resume


async def get_resumes() -> ResumeCollection:
    collection = mongodb.get_collection("resume")
    list_resumes = await collection.find().to_list(length=10)
    return ResumeCollection(resumes=list_resumes)
