from .schema import ResumeModel, ResumeCollection
from ...database import mongodb


async def create_resume(resume: ResumeModel) -> ResumeModel:
    collection = mongodb.get_collection("resume")
    new_resume = await collection.insert_one(
        resume.model_dump(by_alias=True, exclude=["id"])
    )
    created_resume = await collection.find_one({"_id": new_resume.inserted_id})
    return created_resume


async def get_resumes() -> ResumeCollection:
    collection = mongodb.get_collection("resume")
    list_resumes = await collection.find().to_list(length=10)
    return ResumeCollection(resumes=list_resumes)
