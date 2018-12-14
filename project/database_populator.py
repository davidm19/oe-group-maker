from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from test_database_setup import Base, Student, engine, Preference

engine = create_engine('sqlite:///database.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

student1 = Student(first_name = "Charlie", last_name = "")
stud_1_pref_1 = Preference(name = "Peter", priority = 1, student_id = 1)
stud_1_pref_2 = Preference(name = 'Paul', priority = 2, student_id = 1)
stud_1_pref_3 = Preference(name = 'Sam', priority = 3, student_id = 1)
stud_1_pref_4 = Preference(name = 'Kelly', priority = 4, student_id = 1)
stud_1_pref_5 = Preference(name = 'Elise', priority = 5, student_id = 1)

session.add(student1)
session.add(stud_1_pref_1)
session.add(stud_1_pref_2)
session.add(stud_1_pref_3)
session.add(stud_1_pref_4)
session.add(stud_1_pref_5)

session.commit()

student2 = Student(first_name = "Peter", last_name = "")
stud_2_pref_1 = Preference(name = 'Kelly', priority = 1, student_id = 2)
stud_2_pref_2 = Preference(name = 'Elise', priority = 2, student_id = 2)
stud_2_pref_3 = Preference(name = 'Sam', priority = 3, student_id = 2)
stud_2_pref_4 = Preference(name = 'Paul', priority = 4, student_id = 2)
stud_2_pref_5 = Preference(name = 'Charlie', priority = 5, student_id = 2)

session.add(student2)
session.add(stud_2_pref_1)
session.add(stud_2_pref_2)
session.add(stud_2_pref_3)
session.add(stud_2_pref_4)
session.add(stud_2_pref_5)

session.commit()

student3 = Student(first_name = "Elise", last_name = "")
stud_3_pref_1 = Preference(name = 'Peter', priority = 1, student_id = 3)
stud_3_pref_2 = Preference(name = 'Sam', priority = 2, student_id = 3)
stud_3_pref_3 = Preference(name = 'Kelly', priority = 3, student_id = 3)
stud_3_pref_4 = Preference(name = 'Charlie', priority = 4, student_id = 3)
stud_3_pref_5 = Preference(name = 'Paul', priority = 5, student_id = 3)

session.add(student3)
session.add(stud_3_pref_1)
session.add(stud_3_pref_2)
session.add(stud_3_pref_3)
session.add(stud_3_pref_4)
session.add(stud_3_pref_5)

session.commit()

student4 = Student(first_name = "Paul", last_name = "")
stud_4_pref_1 = Preference(name = 'Elise', priority = 1, student_id = 4)
stud_4_pref_2 = Preference(name = 'Charlie', priority = 2, student_id = 4)
stud_4_pref_3 = Preference(name = 'Sam', priority = 3, student_id = 4)
stud_4_pref_4 = Preference(name = 'Peter', priority = 4, student_id = 4)
stud_4_pref_5 = Preference(name = 'Kelly', priority = 5, student_id = 4)

session.add(student4)
session.add(stud_4_pref_1)
session.add(stud_4_pref_2)
session.add(stud_4_pref_3)
session.add(stud_4_pref_4)
session.add(stud_4_pref_5)

session.commit()

student5 = Student(first_name = "Kelly", last_name = "")
stud_5_pref_1 = Preference(name = 'Peter', priority = 1, student_id = 5)
stud_5_pref_2 = Preference(name = 'Charlie', priority = 2, student_id = 5)
stud_5_pref_3 = Preference(name = 'Sam', priority = 3, student_id = 5)
stud_5_pref_4 = Preference(name = 'Elise', priority = 4, student_id = 5)
stud_5_pref_5 = Preference(name = 'Paul', priority = 5, student_id = 5)

session.add(student5)
session.add(stud_5_pref_1)
session.add(stud_5_pref_2)
session.add(stud_5_pref_3)
session.add(stud_5_pref_4)
session.add(stud_5_pref_5)

session.commit()

student6 = Student(first_name = "Sam", last_name = "")
stud_6_pref_1 = Preference(name = 'Charlie', priority = 1, student_id = 6)
stud_6_pref_2 = Preference(name = 'Paul', priority = 2, student_id = 6)
stud_6_pref_3 = Preference(name = 'Kelly', priority = 3, student_id = 6)
stud_6_pref_4 = Preference(name = 'Elise', priority = 4, student_id = 6)
stud_6_pref_5 = Preference(name = 'Peter', priority = 5, student_id = 6)

session.add(student6)
session.add(stud_6_pref_1)
session.add(stud_6_pref_2)
session.add(stud_6_pref_3)
session.add(stud_6_pref_4)
session.add(stud_6_pref_5)

session.commit()
