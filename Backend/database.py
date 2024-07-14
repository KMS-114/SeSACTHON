from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import contextlib

'''
데이터베이스 설정 파일
DB 기본 연결 접속 등을 관리

ORM(object relational mapping)
사용시 DB종류에 상관 없이 코드 일관되게 사용 가능
'''


# SQLAlchemy
DB_URL = "sqlite:///./fastapi.db"

# DB 커넥션 풀 생성 -> 여러 쓰레드가 DB 접근 가능
engine = create_engine(DB_URL, 
                       pool_size=50,
                       connect_args={"check_same_thread":False})

# DB접속을 위한 클래스
SessionLocal = sessionmaker(autocommit=False,
                            autoflush=False,
                            bind=engine)
# Base 클래스는 DB 모델 구성할 때 사용
Base = declarative_base()

# 재너레이터로 생성
@contextlib.contextmanager
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
       

# Async database

async def get_async_db():
    db = AsyncSession(bind=async_engine)
    try:
        yield db
    finally:
        await db.close()