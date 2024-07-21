from bson.objectid import ObjectId
from fastapi import HTTPException
from pymongo import ReturnDocument
from pymongo.errors import PyMongoError

from ...database import mongodb
from .schema import ResumeModel, ResumeCollection


collection = mongodb.get_collection("resume")


async def create(resume: ResumeModel):
    try:
        existing_resume = await collection.find_one({"username": resume.username,
                                                     "jobPostingId": resume.jobPostingId})
        if not existing_resume:
            new_resume = await collection.insert_one(resume.model_dump())
            created_resume = await collection.find_one({"_id": new_resume.inserted_id})
            return ResumeModel(**created_resume)
        else:
            print(f"Resume with username {resume.username} and jobPostingId {resume.jobPostingId} already exists.")
            return None

    except PyMongoError as e:
        print(f"Database error occurred: {e}")
        raise HTTPException(status_code=500, detail="Database error occurred")
    except Exception as e:
        print(f"Unexpected error occurred: {e}")
        raise HTTPException(status_code=500, detail="Unexpected error occurred")


async def update(resume: ResumeModel):
    try:
        existing_profile = await collection.find_one({"username": resume.username, "jobPostingId": resume.jobPostingId})
        if not existing_profile:
            return None
        else:
            new_resume = await collection.find_one_and_update(
                {"username": resume.username, "jobPostingId": resume.jobPostingId},
                {"$set": resume.model_dump()},
                return_document=ReturnDocument.AFTER,
            )
            return ResumeModel(**new_resume)
    except Exception as e:
        print(f"Error updating profile: {e}")
        return None

async def get(username: str, jobPostingId: str):
    try:
        resume_data = collection.find_one({"username": username, "jobPostingId": jobPostingId})
        if resume_data:
            return ResumeModel(**resume_data)
        else:
            return None
    except Exception as e:
        print(f"Error find {username}'s resume")


async def get_all() -> ResumeCollection:
    list_resumes = await collection.find().to_list()
    return ResumeCollection(resumes=list_resumes)

async def delete(username: str, jobPostingId: str):
    try:
        delete_result = await collection.delete_one({"username": username,
                                                     "jobPostingId": jobPostingId})
        if delete_result.deleted_count == 1:
            return 'Document successfully deleted.'
        else:
            return 'No document found to delete.'
    except PyMongoError as e:
        raise RuntimeError("Database error occured")
    except Exception as e:
        raise RuntimeError("Unexpected error occured")

