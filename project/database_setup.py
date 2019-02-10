import sys
from sqlalchemy import Table, Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship, backref
from sqlalchemy.sql import func

Base = declarative_base()

trip_student_link = Table('trip_student_link', Base.metadata,
    Column('trip_id', Integer, ForeignKey('trip.id')),
    Column('student_id', Integer, ForeignKey('student.id'))
    )

class Trip(Base):
    __tablename__ = 'trip'
    id = Column(Integer, primary_key=True, autoincrement=True)
    trip_name = Column(String(32))
    trip_grade = Column(String(2))
    students = relationship('Student',secondary=trip_student_link,
                             back_populates="trips")
    @property
    def serialize(self):
        return {
            'id': self.id,
            'trip_name': self.trip_name,
            'trip_grade': self.trip_grade,
            'students': [student.serialize for student in self.students]
        }

class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(32))
    last_name = Column(String(32))
    grade = Column(Integer, nullable = False)
    trips = relationship('Trip', secondary=trip_student_link,
                          back_populates="students")

    @property
    def serialize(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'grade': self.grade
        }


class Preference(Base):
    __tablename__ = 'preference'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(32))
    priority = Column(Integer)
    student_id = Column(Integer, ForeignKey('student.id'))
    student = relationship(Student)

engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
