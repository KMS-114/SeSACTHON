from typing import Optional

from datetime import datetime
from pydantic import BaseModel, Field

from ...database import PyObjectId
from ..job_posting.schema import CoverLetterQuestion
from ..profile.schema import ProfileModel


class CoverLetter(BaseModel):
    question: CoverLetterQuestion
    answer: str


class ResumeModel(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    userId: str
    jobPostingId: str

    profile: ProfileModel
    coverLetters: list[CoverLetter]

    createdAt: datetime
    updatedAt: datetime


class ResumeCollection(BaseModel):
    resumes: list[ResumeModel]
