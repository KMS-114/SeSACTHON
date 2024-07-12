'''
DB 클래스 정의

'''

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, SmallInteger, String, Date, ForeignKey

Base = declarative_base()


class TbUser(Base):
    __tablename__ = 'user'
    userId = Column('userId', Integer, primary_key=True)
    userGroup = Column('userGroup', SmallInteger)
    username = Column('username', String(20))
    password = Column('password', String(20))
    affiliation = Column('affiliation', String(20))


class TbProfile(Base):
    __tablename__ = 'profile'
    userId = Column('userId', Integer, ForeignKey('user.userId'), primary_key=True)
    name = Column('name', String(30))
    birth = Column('birth', Date),
    gender = Column('gender', SmallInteger)


class TbJobPosting(Base):
    __tablename__ = 'jobPosting'
    jobPostingId = Column('jobPostingId', Integer, primary_key=True)
    userId = Column('userId', Integer, ForeignKey('user.userId'))
    title = Column('title', String(50))
    description = Column('description', String(100))


class TbResume(Base):
    __tablename__ ='resume'
    userId = Column('userId',
                    Integer,
                    ForeignKey('user.userId'),
                    primary_key=True)
    jobPostingId = Column('jobPostingId',
                          Integer,
                          ForeignKey('jobPosting.jobPostingId'),
                          primary_key=True)
