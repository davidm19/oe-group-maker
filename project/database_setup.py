import sys
from sqlalchemy import Table, Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.sql import func

Base = declarative_base()
#
association_table = Table('association', Base.metadata,
    Column('trip_id', Integer, ForeignKey('trip.id')),
    Column('student_id', Integer, ForeignKey('student.id'))
)

class Trip(Base):
    __tablename__ = 'trip'
    id = Column(Integer, primary_key=True, autoincrement=True)
    trip_name = Column(String(32))
    trip_grade = Column(Integer)
    students = relationship('Student',secondary=association_table, backref='students', lazy='dynamic')

class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(32))
    last_name = Column(String(32))
    grade = Column(Integer, nullable = False)
    # trip_id = Column(Integer, ForeignKey('trip.id'))
    # trips = relationship('Trip', backref='student')

    @property
    def serialize(self):
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'grade': self.grade,
            # 'trip_id': self.trip_id
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
