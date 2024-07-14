from typing import Optional
from datetime import datetime

from pydantic import BaseModel, Field

from ...database import PyObjectId


class QualificationRequired(BaseModel):
    ageMin: int
    ageMax: int
    gender: int
    customQualification: dict[str, str]


class CoverLetterQuestion(BaseModel):
    content: str
    charLimit: int


class JobPostingModel(BaseModel):
    id: Optional[PyObjectId] = Field(alias='_id', default=None)
    userId: str
    title: str
    description: str

    qualificationsRequired: QualificationRequired
    coverLetterQuestions: list[CoverLetterQuestion]

    createdAt: datetime
    updatedAt: datetime


class JobPostingCollection(BaseModel):
    jobPostings: list[JobPostingModel]
