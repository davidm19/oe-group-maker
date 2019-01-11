from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, Trip, Student, engine, Preference

engine = create_engine('sqlite:///database.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

JTree = Trip(trip_name="JTree", trip_grade='7')
session.add(JTree)
session.commit()

John = Student(first_name='John', last_name='Doe', grade='7', trip=JTree)
session.add(John)
session.commit()


Jane = Student(first_name='Jane', last_name='Doe', grade='7', trip=JTree)
session.add(Jane)

#
# Mia = Student(first_name='Mia', last_name='Dimson', grade='7')
# session.add(Mia)
#
#
# David = Student(first_name='David', last_name='Malone', grade='7')
# session.add(David)
#
#
# Michael = Student(first_name='Michael', last_name='Huang', grade='7')
# session.add(Michael)


session.commit()
