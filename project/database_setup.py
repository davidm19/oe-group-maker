import sys
from sqlalchemy import Table, Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship, backref
from sqlalchemy.sql import func

Base = declarative_base()

class Student(Base):
    __tablename__ = 'student'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))
    grade = Column(Integer, nullable=True)
    first_name = Column(String(32))
    last_name = Column(String(32))
    gender = Column(String(32))
    has_chosen_preferences = Column(Boolean, default=False)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'gender': self.gender,
            'has_chosen_preferences': self.has_chosen_preferences
        }


class Preference(Base):
    __tablename__ = 'preference'

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name1 = Column(String(32))
    last_name1 = Column(String(32))
    name = Column(String(100), nullable=False)
    gender = Column(String(32))
    student_id = Column(Integer, ForeignKey('student.id'))
    student = relationship(Student)
    preference_id = Column(Integer)

engine = create_engine('sqlite:///outdoor-ed.db')
Base.metadata.create_all(engine)
