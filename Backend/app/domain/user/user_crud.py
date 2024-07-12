'''
데이터베이스 처리 파일

데이터 CRUD  처리

'''
from sqlalchemy.orm import Session

from ...models import TbUser
from .user_schema import User


def create_user(db: Session, user: User) -> TbUser:
    db_user = TbUser(
        userId=user.userId, userGroup=user.userGroup,
        username=user.username, password=user.password,
        affilication=user.affiliation,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
