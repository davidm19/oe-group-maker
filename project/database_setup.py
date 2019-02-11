import sys
from sqlalchemy import Table, Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.sql import func
import argparse

Base = declarative_base()

association_table = Table('association', Base.metadata,
                          Column('trip_id', Integer, ForeignKey('trip.id')),
                          Column('student_id', Integer,
                                 ForeignKey('student.id'))
                          )


class Trip(Base):
    __tablename__ = 'trip'
    id = Column(Integer, primary_key=True, autoincrement=True)
    trip_name = Column(String(32))
    trip_grade = Column(Integer)
    students = relationship('Student', secondary=association_table,
                            back_populates="trips")

    @property
    def serialize(self):
        return {
            'trip_name': self.trip_name,
            'trip_grade': self.trip_grade,
            'students': self.students
        }
    # students = relationship('Student', secondary='student_trip_link')
    # trip_grade = Column(String(2))


class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(32))
    last_name = Column(String(32))
    grade = Column(Integer, nullable=False)
    trips = relationship('Trip', secondary=association_table,
                         back_populates="students")
    # trip = relationship('Trip', secondary='student_trip_link')

    @property
    def serialize(self):
        return {
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


parser = argparse.ArgumentParser()
parser.add_argument("-t", "--test", action="store_true")
args = parser.parse_args()
if args.test:
    print "Created test database"
    engine = create_engine('sqlite:///test.db')
else:
    print "Created regular database"
    engine = create_engine('sqlite:///database.db')

Base.metadata.create_all(engine)

# engine = create_engine('sqlite:///database.db')
# Base.metadata.create_all(engine)
