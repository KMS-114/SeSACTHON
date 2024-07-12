from sqlalchemy.orm import Session
from pymongo.database import Database

from ...models import TbJobPosting
from .job_posting_schema import JobPosting


def create_job_posting(
    db: Session,
    mongo: Database,
    job_posting: JobPosting
) -> tuple[TbJobPosting, dict]:

    db_job_posting = TbJobPosting(
        jobPostingId=job_posting.jobPostingId,
        userId=job_posting.userId,
        title=job_posting.title,
        description=job_posting.description,
    )
    db.add(db_job_posting)
    db.commit()
    db.refresh(db_job_posting)

    doc = {
        "jobPostingId": job_posting.jobPostingId,
        "userId": job_posting.userId,
        "content": {
            "title": job_posting.title,
            "description": job_posting.description,
            "qualificationsRequired": job_posting.qualificationsRequired.dict(),
            "coverLetterQuestions": [item.dict() for item in job_posting.coverLetterQuestions]
        },
        "createdAt": job_posting.createdAt,
        "updatedAt": job_posting.updatedAt,
    }
    collection = mongo.get_collection('jobPosting')
    collection.insert_one(doc)
    return db_job_posting, doc
