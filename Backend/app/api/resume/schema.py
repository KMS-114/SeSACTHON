from typing import Optional, Union

from datetime import datetime
from pydantic import BaseModel, Field

from ...database import PyObjectId
from ..profile.schema import ProfileModel


class CoverLetter(BaseModel):
    questionId: int
    answer: str


class ResumeModel(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    username: str       # PK처럼 사용
    jobPostingId: str

    coverLetters: list[CoverLetter]

    createdAt: datetime
    updatedAt: datetime


class ResumeCollection(BaseModel):
    resumes: list[ResumeModel]
