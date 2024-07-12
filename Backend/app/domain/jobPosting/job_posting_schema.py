from pydantic import BaseModel
from datetime import datetime


class QualificationRequired(BaseModel):
    ageMin: int
    ageMax: int
    gender: int
    customQualification: dict[str, str]


class CoverLetterQuestion(BaseModel):
    content: str
    charLimit: int


class JobPosting(BaseModel):
    jobPostingId: int
    userId: int
    title: str
    description: str

    qualificationsRequired: QualificationRequired
    coverLetterQuestions: list[CoverLetterQuestion]

    createdAt: datetime
    updatedAt: datetime
