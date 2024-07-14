from .schema import JobPostingModel, JobPostingCollection
from ...database import mongodb


async def create_job_posting(
    job_posting: JobPostingModel
) -> JobPostingModel:
    collection = mongodb.get_collection("jobPosting")
    new_job_posting = await collection.insert_one(
        job_posting.model_dump(by_alias=True, exclude=["id"])
    )
    created_job_posting = await collection.find_one(
        {"_id": new_job_posting.inserted_id}
    )
    return created_job_posting


async def get_job_postings():
    collection = mongodb.get_collection("jobPosting")
    list_job_postings = await collection.find().to_list(length=10)
    return JobPostingCollection(jobPostings=list_job_postings)
