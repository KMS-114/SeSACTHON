from sqlalchemy.orm import Session
from models import User, Profile
from schemas import UserCreate, ProfileCreate

def create_user(db: Session, user: UserCreate):
    db_user = User(username=user.username, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_profile(db: Session, profile: ProfileCreate):
    db_profile = Profile(
        name=profile.name,
        gender=profile.gender,
        birthdate=profile.birthdate,
        phone=profile.phone,
        residence=profile.residence,
    )

    db.add(db_profile)
    db.commit()
    db.refresh(db_profile)
    return db_profile

def get_user(db:Session, userId: str):
    return db.query(User).filter(User.userId == userId).first()
def get_profile(db: Session, userId: str):
    return db.query(Profile).filter(Profile.userId == userId).all()