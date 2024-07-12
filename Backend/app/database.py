'''
데이터베이스 설정 파일
DB 기본 연결 접속 등을 관리

ORM(object relational mapping)
사용시 DB종류에 상관 없이 코드 일관되게 사용 가능
'''

import sqlalchemy
from sqlalchemy.orm import sessionmaker, Session
from pymongo import MongoClient


def get_rdb_session() -> Session:
    try:
        engine = sqlalchemy.create_engine('sqlite:////database/sqlite/sqlite3.db')
        session = sessionmaker(bind=engine)()
        return session
    finally:
        session.close()


def get_mongo_database() -> MongoClient:
    client = MongoClient("http://172.17.0.2:27017/")
    db = client.get_database("hackerton")
    return db

# Async database
# async def get_async_db():
#     db = AsyncSession(bind=async_engine)
#     try:
#         yield db
#     finally:
#         await db.close()