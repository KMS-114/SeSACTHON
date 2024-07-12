from sqlalchemy.orm import Session
from pymongo.database import Database

from ...models import TbProfile
from .profile_schema import Profile


def create_profile(db: Session, mongo: Database, profile: Profile) -> tuple[TbProfile, dict]:
    db_profile = TbProfile(**profile.dict())
    db.add(db_profile)
    db.commit()
    db.refresh(db_profile)

    collection = mongo.get_collection('profile')
    doc = {
        "userId": profile.userId,
        "content": {
            "name": profile.name,
            "birth": profile.birth,
            "gender": profile.gender,
            "skills": profile.skills,
            "careers": [item.dict() for item in profile.careers]
        },
        "createdAt": profile.createdAt,
        "updatedAt": profile.updatedAt,
    }
    collection.insert_one(doc)

    return db_profile, doc
