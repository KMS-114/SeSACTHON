'''
DB 클래스 정의

'''

from sqlalchemy import Column, Integer, String, Date, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__="users"

    userId = Column(String, primary_key=True, index=True)
    password = Column(String)
    profiles = relationship("Profile", back_populates="user")

class Profile(Base):
    __tablename__ = "profiles"

    # id = Column(Integer, primary_key=True, index=True)
    userId = Column(String, ForeignKey('users.userId'), primary_key=True)
    name = Column(String, index=True)
    gender = Column(String, index=True)
    birthdate = Column(Date)
    phone = Column(String, index=True)
    residence = Column(String, index=True)
    certificates = Column(String)
    user = relationship("User", back_populates="profiles")

