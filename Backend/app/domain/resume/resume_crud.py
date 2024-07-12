from sqlalchemy.orm import Session
from pymongo.database import Database

from ...models import TbResume
from .resume_schema import Resume


def create_resume(db: Session,
                  mongo:Database,
                  resume: Resume) -> tuple[TbResume, dict]:
    db_resume = TbResume(
        userId=resume.userId,
        jobPostingId=resume.jobPostingId
    )
    db.add(db_resume)
    db.commit()
    db.refresh(db_resume)

    collection = mongo.get_collection('resume')
    doc = {
        "userId": resume.userId,
        "jobPostingId": resume.jobPostingId,
        "coverLetters": [item.dict() for item in resume.coverLetters],
    }
    collection.insert_one(doc)
    return db_resume, doc
