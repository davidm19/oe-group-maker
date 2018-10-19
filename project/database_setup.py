import sys
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func

Base = declarative_base()

class Student(Base):
    __tablename__ = 'student'

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(32))
    last_name = Column(String(32))
    preferred_member1 = Column(String(32))
    preferred_member2 = Column(String(32))
    preferred_member3 = Column(String(32))

class PreferredMember(Base):
    __tablename__ = 'preferred_member'
    id = Column(Integer, primary_key=True, autoincrement=True)
    priority = Column(String(10))

engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
