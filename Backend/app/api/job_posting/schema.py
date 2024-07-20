from typing import Optional, Union
from datetime import datetime

from pydantic import BaseModel, Field

from ...database import PyObjectId
from ..resume.schema import ResumeCollection


class QualificationRequired(BaseModel):
    ageMin: int
    ageMax: int
    gender: int
    customQualification: dict[str, str]


class CoverLetterQuestion(BaseModel):
    coverLetterQuestionId: int
    content: str
    charLimit: int


class JobPostingModel(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    username: str   # pk처럼 사용
    title: str
    description: str

    qualificationsRequired: QualificationRequired
    coverLetterQuestions: list[CoverLetterQuestion]

    createdAt: datetime
    updatedAt: datetime


class JobPostingCollection(BaseModel):
    jobPostings: list[JobPostingModel]
