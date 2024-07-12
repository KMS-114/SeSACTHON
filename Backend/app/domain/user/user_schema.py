'''
입출력 관리 파일

입출력 데이터의 스펙 정의 및 검증
'''
from pydantic import BaseModel


class User(BaseModel):
    userId: str
    userGroup: int

    username: str
    password: str
    affiliation: str
