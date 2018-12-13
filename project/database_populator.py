from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, Trip, Student, engine, Preference

engine = create_engine('sqlite:///database.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# student1 = Student(first_name = "Michael", last_name = "Huang", grade = 11)
slevy = Student(first_name = "Sammy", last_name = "Levy", grade = 11)
serena = Student(first_name = "Serena", last_name = "Hingorani", grade = 11)
sbernstein = Student(first_name = "Sammy", last_name = "Bernstein", grade = 11)
noah = Student(first_name = "Noah", last_name = "Rizika", grade = 11)
wyatt = Student(first_name = "Wyatt", last_name = "Wagner", grade = 11)
dawson = Student(first_name = "Dawson", last_name = "Goldsmith", grade = 11)
christina = Student(first_name = "Christina", last_name = "Bruni", grade = 11)
# student1 = Student(first_name = "Michael", last_name = "Huang")
# stud_1_pref_1 = Preference(name = "JD", priority = 1, student_id = 1)

# session.add(student1)
# session.add(stud_1_pref_1)
session.add(slevy)
session.add(serena)
session.add(sbernstein)
session.add(noah)
session.add(wyatt)
session.add(dawson)
session.add(christina)

session.add(student1)
session.add(stud_1_pref_1)
# session.commit()

student2 = Student(first_name = "J", last_name = "D", grade=11)
stud_2_pref_1 = Preference(name = 'Michael', priority = 1, student_id = 2)
stud_2_pref_2 = Preference(name = 'Ryan', priority = 2, student_id = 2)
stud_2_pref_3 = Preference(name = 'David', priority = 3, student_id = 2)

# session.add(student2)
# session.add(stud_2_pref_1)
# session.add(stud_2_pref_2)
# session.add(stud_2_pref_3)
# session.commit()

trip1 = Trip(trip_name="Kern County", trip_grade="11")
# trip2 = Trip(trip_name="Catalina Trip")
# trip3 = Trip(trip_name="Kern River")
# trip4 = Trip(trip_name="Joshua Tree")

session.add(trip1)
# session.add(trip2)
# session.add(trip3)
# session.add(trip4)
session.commit()
