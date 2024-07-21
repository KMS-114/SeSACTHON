from typing import Union

from pydantic import BaseModel, Field
from datetime import datetime, timezone



class Career(BaseModel):
    startDate: datetime
    endDate: Union[datetime, None] = Field(default=None)
    affiliation: str
    summary: str


class ProfileModel(BaseModel):
    username: str   # pk처럼 사용

    name: str
    birth: datetime
    gender: int

    skills: list[str]
    careers: list[Career]

    createdAt: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updatedAt: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class ProfileCollection(BaseModel):
    profiles: list[ProfileModel]
