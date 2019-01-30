from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, Trip, Student, engine, Preference

engine = create_engine('sqlite:///database.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# student1 = Student(first_name = "Michael", last_name = "Huang", grade = 11)
student1 = Student(first_name = "Michael", last_name = "Huang", grade = "7")
student2 = Student(first_name = "Mia", last_name = "Dimson", grade = "7")
student3 = Student(first_name = "David", last_name = "Malone", grade = "7")
student4 = Student(first_name = "Ryan", last_name = "Hom", grade = "7")
# stud_1_pref_1 = Preference(name = "JD", priority = 1, student_id = 1)


session.add(student1)
session.add(student2)
session.add(student3)
session.add(student4)

# session.add(stud_1_pref_1)
session.commit()

student2 = Student(first_name = "J", last_name = "D", grade = 11)
# student2 = Student(first_name = "J", last_name = "D")
stud_2_pref_1 = Preference(name = 'Michael', priority = 1, student_id = 2)
stud_2_pref_2 = Preference(name = 'Ryan', priority = 2, student_id = 2)
stud_2_pref_3 = Preference(name = 'David', priority = 3, student_id = 2)

session.add(student2)
session.add(stud_2_pref_1)
session.add(stud_2_pref_2)
session.add(stud_2_pref_3)
session.commit()

trip1 = Trip(trip_name="Death Valley Backpacking", trip_grade = "9")
trip2 = Trip(trip_name="Montana De Oro", trip_grade = "7")
trip3 = Trip(trip_name="Joshua Tree Backpacking", trip_grade = "9")
trip4 = Trip(trip_name="Joshua Tree", trip_grade = "7")

session.add(trip1)
# session.add(trip2)
# session.add(trip3)
# session.add(trip4)
session.commit()
