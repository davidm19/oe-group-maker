import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.sql import func

Base = declarative_base()

class Trip(Base):
    __tablename__ = 'trip'
    id = Column(Integer, primary_key=True, autoincrement=True)
    trip_name = Column(String(32))
    students = relationship('Trip', secondary='student_trip_link')

class Student(Base):
    __tablename__ = 'student'

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(32))
    last_name = Column(String(32))
    grade = Column(Integer, nullable = False)
    trip = relationship('Student', secondary='student_trip_link')
    # trip_id = Column(Integer, ForeignKey('trip.id'), nullable = True)

    @property
    def serialize(self):
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'grade': self.grade
        }

class student_trip_link(Base):
    __tablename__ = 'student_trip_link'
    student_id = Column(Integer, ForeignKey('student.id') primary_key = True)
    trip_id = Column(Integer, ForeignKey('trip.id'), primary_key = True)

class Preference(Base):
    __tablename__ = 'preference'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(32))
    priority = Column(Integer)
    student_id = Column(Integer, ForeignKey('student.id'))
    student = relationship(Student)

engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
