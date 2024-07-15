from .schema import JobPostingModel, JobPostingCollection
from ...database import mongodb


async def create_job_posting(job_posting: JobPostingModel) -> JobPostingModel:
    collection = mongodb.get_collection("jobPosting")
    new_job_posting = await collection.insert_one(
        job_posting.model_dump(by_alias=True, exclude=["id"])
    )
    created_job_posting = await collection.find_one(
        {"_id": new_job_posting.inserted_id}
    )
    return created_job_posting


async def find_all_job_postings() -> JobPostingCollection:
    collection = mongodb.get_collection("jobPosting")
    list_job_postings = await collection.find().to_list(length=10)
    return JobPostingCollection(jobPostings=list_job_postings)


async def find_job_posting(job_posting_id: str) -> JobPostingModel:
    collection = mongodb.get_collection("jobPosting")
    job_posting = await collection.find_one({"_id": job_posting_id})
    return JobPostingModel(**job_posting)


async def delete_job_posting(job_posting_id: str):
    collection = mongodb.get_collection("jobPosting")
    dropped_posting = await find_job_posting(job_posting_id)
    if dropped_posting:
        result = await collection.delete_one({"_id": job_posting_id})
    return dropped_posting
