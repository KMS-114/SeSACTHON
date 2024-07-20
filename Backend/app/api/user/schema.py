from typing import Optional
from datetime import datetime

from pydantic import BaseModel, Field

from ...database import PyObjectId


class UserModel(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    userGroup: int

    username: str       # PK처럼 사용
    password: str
    affiliation: str

    createdAt: datetime
    updatedAt: datetime


class UserCollection(BaseModel):
    users: list[UserModel]
