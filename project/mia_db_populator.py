from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, Trip, Student, engine, Preference

engine = create_engine('sqlite:///database.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

JTree = Trip(trip_name="JTree", trip_grade='7')
session.add(JTree)

Trip2 = Trip(trip_name="Montana De Oro", trip_grade='7')
session.add(Trip2)
session.commit()


John = Student(first_name='John', last_name='Doe', grade='7')
session.add(John)
Jane = Student(first_name='Jane', last_name='Doe', grade='7')
session.add(Jane)
Mia = Student(first_name='Mia', last_name='Dimson', grade='7')
session.add(Mia)
David = Student(first_name='David', last_name='Malone', grade='7')
session.add(David)
Michael = Student(first_name='Michael', last_name='Huang', grade='7')
pref_1 = Preference(student=David)
Michael.preferences.append(pref_1)
session.add(Michael)
session.commit()


JTree.students.append(John)
JTree.students.append(Jane)
JTree.students.append(David)

Trip2.students.append(Mia)
Trip2.students.append(Michael)
Trip2.students.append(Jane)
Trip2.students.append(John)



session.commit()
