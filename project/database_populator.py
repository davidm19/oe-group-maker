from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from test_database_setup import Base, Trip, Student, engine, Preference

engine = create_engine('sqlite:///database.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

student1 = Student(first_name = "Michael", last_name = "Huang", grade=11)
stud_1_pref_1 = Preference(name = "JD", priority = 1, student_id = 1)

session.add(student1)
session.add(stud_1_pref_1)
# session.commit()

student2 = Student(first_name = "J", last_name = "D", grade=11)
stud_2_pref_1 = Preference(name = 'Michael', priority = 1, student_id = 2)
stud_2_pref_2 = Preference(name = 'Ryan', priority = 2, student_id = 2)
stud_2_pref_3 = Preference(name = 'David', priority = 3, student_id = 2)

session.add(student2)
session.add(stud_2_pref_1)
session.add(stud_2_pref_2)
session.add(stud_2_pref_3)
# session.commit()

trip1 = Trip(name="Death Valley Backpacking")
trip2 = Trip(name="Catalina Trip")
trip3 = Trip(name="Kern River")

session.add(trip1)
session.add(trip2)
session.add(trip3)
session.commit()
