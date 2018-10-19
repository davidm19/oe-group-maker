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
    priority1 = Column(String(32))
    preferred_member2 = Column(String(32))
    priority2 = Column(String(32))
    preferred_member3 = Column(String(32))
<<<<<<< HEAD:project/database_setup.py
    priority3 = Column(String(32))
=======
    priority3 = Column(String(32))
>>>>>>> development

engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
