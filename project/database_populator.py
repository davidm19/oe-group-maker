from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, Trip, Student, engine, Preference
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--test", action="store_true")
args = parser.parse_args()
if args.test:
    print "Populated test database"
    engine = create_engine('sqlite:///test.db')
else:
    print "Populated permanent database"
    engine = create_engine('sqlite:///database.db')

# engine = create_engine('sqlite:///database.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

student1 = Student(first_name="Michael", last_name="Huang", grade="7")
student2 = Student(first_name="Mia", last_name="Dimson", grade="7")
student3 = Student(first_name="David", last_name="Malone", grade="7")
student4 = Student(first_name="Ryan", last_name="Hom", grade="7")


session.add(student1)
session.add(student2)
session.add(student3)
session.add(student4)

session.commit()

trip1 = Trip(trip_name="Death Valley Backpacking", trip_grade="9")
trip2 = Trip(trip_name="Montana De Oro", trip_grade="7")
trip3 = Trip(trip_name="Joshua Tree Backpacking", trip_grade="9")
trip4 = Trip(trip_name="Joshua Tree", trip_grade="7")

session.add(trip1)
session.add(trip2)
session.add(trip3)
session.add(trip4)
session.commit()
