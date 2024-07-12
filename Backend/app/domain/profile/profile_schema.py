from pydantic import BaseModel
from datetime import date


class Career(BaseModel):
    startDate: date
    endDate: date
    affilication: str
    summary: str


class Profile(BaseModel):
    profileId: int
    userId: int

    name: str
    birth: date
    gender: int

    skills: list[str] = []
    careers: list[Career] = []

    createdAt: date
    updatedAt: date = None
