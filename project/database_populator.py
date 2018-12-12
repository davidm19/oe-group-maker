from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from test_database_setup import Base, Student, engine, Preference

engine = create_engine('sqlite:///database.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

student1 = Student(first_name = "Michael", last_name = "Huang")
stud_1_pref_1 = Preference(name = "David", priority = 1, student_id = 1)
stud_1_pref_2 = Preference(name = 'Ryan', priority = 2, student_id = 1)
stud_1_pref_3 = Preference(name = 'Frank', priority = 3, student_id = 1)

session.add(student1)
session.add(stud_1_pref_1)
session.add(stud_1_pref_2)
session.add(stud_1_pref_3)

session.commit()

student2 = Student(first_name = "David", last_name = "Malone")
stud_2_pref_1 = Preference(name = 'Frank', priority = 1, student_id = 2)
stud_2_pref_2 = Preference(name = 'Ryan', priority = 2, student_id = 2)
stud_2_pref_3 = Preference(name = 'Michael', priority = 3, student_id = 2)

session.add(student2)
session.add(stud_2_pref_1)
session.add(stud_2_pref_2)
session.add(stud_2_pref_3)

session.commit()

student3 = Student(first_name = "Ryan", last_name = "Hom")
stud_3_pref_1 = Preference(name = 'David', priority = 1, student_id = 3)
stud_3_pref_2 = Preference(name = 'Frank', priority = 2, student_id = 3)
stud_3_pref_3 = Preference(name = 'Michael', priority = 3, student_id = 3)

session.add(student3)
session.add(stud_3_pref_1)
session.add(stud_3_pref_2)
session.add(stud_3_pref_3)

session.commit()

student4 = Student(first_name = "Frank", last_name = "Glantz") 
stud_4_pref_1 = Preference(name = 'Michael', priority = 1, student_id = 4)
stud_4_pref_2 = Preference(name = 'David', priority = 2, student_id = 4)
stud_4_pref_3 = Preference(name = 'Ryan', priority = 3, student_id = 4)

session.add(student4)
session.add(stud_4_pref_1)
session.add(stud_4_pref_2)
session.add(stud_4_pref_3)

session.commit()
