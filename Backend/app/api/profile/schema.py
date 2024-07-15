from typing import Union

from pydantic import BaseModel, Field
from datetime import datetime


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

    skills: list[str]
    careers: list[Career]

    createdAt: datetime
    updatedAt: datetime


class ProfileCollection(BaseModel):
    profiles: list[ProfileModel]