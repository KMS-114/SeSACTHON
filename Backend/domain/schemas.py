from pydantic import BaseModel
from typing import List,Optional
from datetime import date

# DB 기본 속성 정의
class UserBase(BaseModel):
    userId: str

# client 반환 속성
class UserCreate(UserBase):
    password: str

# DB 저장될 속성
class User(UserBase):
    class Config:
        orm_mode: True


class ProfileBase(BaseModel):
    name: str
    gender: str
    birthdate: date
    phone: str
    residence: str
    certificates: str

class ProfileCreate(ProfileBase):
    userId: str

class Profile(ProfileBase):
    userId: str
    user: User

    class Config:
        orm_mode: True


# class ExperienceBase(BaseModel):
#     start_date: date
#     end_date: date
#     position: str
#     description: str
#
# class ExperienceCreate(ExperienceBase):
#     pass
#
# class Experience(ExperienceBase):
#     id: int
#     user_id: int
#
#     class Config:
#         orm_mode: True
