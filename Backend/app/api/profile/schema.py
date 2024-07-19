from typing import Union

from pydantic import BaseModel, Field
from datetime import datetime, timezone


class Skill(BaseModel):
    acquisition_date: str
    qualification: str

class Career(BaseModel):
    startDate: datetime
    endDate: Union[datetime, None] = Field(default=None)
    affiliation: str
    summary: str


class ProfileModel(BaseModel):
    userId: str

    name: str
    birth: datetime
    gender: int

    skills: list[Skill]
    careers: list[Career]

    createdAt: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updatedAt: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class ProfileCollection(BaseModel):
    profiles: list[ProfileModel]
