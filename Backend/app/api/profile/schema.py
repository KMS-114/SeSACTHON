from pydantic import BaseModel
from datetime import date, datetime


class Career(BaseModel):
    startDate: date
    endDate: date
    affilication: str
    summary: str


class ProfileModel(BaseModel):
    userId: str

    name: str
    birth: date
    gender: int

    skills: list[str] = []
    careers: list[Career] = []

    createdAt: datetime
    updatedAt: datetime


class ProfileCollection(BaseModel):
    profiles: list[ProfileModel]
