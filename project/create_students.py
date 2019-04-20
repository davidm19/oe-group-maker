import csv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, Student, engine, Preference

engine = create_engine('sqlite:///outdoor-ed.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

with open('12th_graders.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    # This skips the first row of the CSV file.
    # csvreader.next() also works in Python 2.
    csvreader.next()

    for row in csvreader:
        student = Student(name=row[0] + ' (' + row[1] + ')', email=row[3], gender=row[4])
        session.add(student)
    
    session.commit()