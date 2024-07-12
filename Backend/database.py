'''
데이터베이스 설정 파일
DB 기본 연결 접속 등을 관리

ORM(object relational mapping)
사용시 DB종류에 상관 없이 코드 일관되게 사용 가능
'''

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite://"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread":False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def init_db():
    Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

