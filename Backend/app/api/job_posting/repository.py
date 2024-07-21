from .schema import JobPostingModel, JobPostingCollection
from bson import ObjectId
from ...database import mongodb
collection = mongodb.get_collection("jobPosting")

async def update_description(job_posting_id:str, description:str)->dict:
    job_posting = await collection.find_one({"_id": ObjectId(job_posting_id)})
    if job_posting is None:
        return {"message": "job_posting_id가 유효하지 않습니다."}

    result = await collection.update_one({"_id": ObjectId(job_posting_id)}, {"$set": {f"description": description}})
    if result.modified_count == 1:
        return {f"message": "description update 완료"}
    
async def update_cover_letter_question(job_posting_id:str, content:str, char_limit:int)->dict:
    job_posting = await collection.find_one({"_id": ObjectId(job_posting_id)})
    if job_posting is None:
        return {"message": "job_posting_id가 유효하지 않습니다."}

    result = await collection.update_one({"_id": ObjectId(job_posting_id)}, {"$push": {f"coverLetterQuestions": {"content": content, "charLimit": char_limit}}})
    if result.modified_count == 1:
        return {f"message": "cover_letter_question update 완료"}

async def update_qualification(job_posting_id:str, key:str, value:str):
    job_posting = await collection.find_one({"_id": ObjectId(job_posting_id)})
    if job_posting is None:
        return {"message": "job_posting_id가 유효하지 않습니다."}

    result = await collection.update_one({"_id": ObjectId(job_posting_id)}, {"$set": {f"qualificationsRequired.customQualification.{key}": value}})
    if result.modified_count == 1:
        return {f"message": "custom_qualification update 완료"}
    
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
    job_posting = await collection.find_one({"_id": ObjectId(job_posting_id)})
    return JobPostingModel(**job_posting)


async def delete_job_posting(job_posting_id: str):
    collection = mongodb.get_collection("jobPosting")
    dropped_posting = await find_job_posting(job_posting_id)
    if dropped_posting:
        result = await collection.delete_one({"_id": job_posting_id})
    return dropped_posting
