import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.sql import func

Base = declarative_base()

class Student(Base):
    __tablename__ = 'student'

    id = Column(Integer, primary_key=True, autoincrement=True)
    # grade = Column(Integer, nullable = True)
    first_name = Column(String(32))
    last_name = Column(String(32))
    name = str(first_name) + str(last_name)
    gender = Column(String(32))


class Preference(Base):
    __tablename__ = 'preference'

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name1 = Column(String(32))
    last_name1 = Column(String(32))
    name = str(first_name1) + str(last_name1)
    gender = Column(String(32))
    student_id = Column(Integer, ForeignKey('student.id'))
    student = relationship(Student)
    preference_id = Column(Integer)

engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
