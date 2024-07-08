'''
데이터베이스 설정 파일
DB 기본 연결 접속 등을 관리

ORM(object relational mapping)
사용시 DB종류에 상관 없이 코드 일관되게 사용 가능
'''



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