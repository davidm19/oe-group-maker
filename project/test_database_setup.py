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
    first_name = Column(String(32))
    last_name = Column(String(32))


class Preference(Base):
    __tablename__ = 'preference'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(32))
    priority = Column(Integer)
    student_id = Column(Integer, ForeignKey('student.id'))
    student = relationship(Student)

engine = create_engine('sqlite:///test_database.db')
Base.metadata.create_all(engine)
