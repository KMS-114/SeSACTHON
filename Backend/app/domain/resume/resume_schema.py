from pydantic import BaseModel
from ..jobPosting.job_posting_schema import CoverLetterQuestion


class CoverLetter(BaseModel):
    question: CoverLetterQuestion
    answer: str


class Resume(BaseModel):
    userId: int
    jobPostingId: int

    coverLetters: list[CoverLetter]
