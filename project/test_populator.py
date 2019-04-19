import barnum
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, Student, engine, Preference

engine = create_engine('sqlite:///test.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

def create_students():
    gender = 'Male'
    for i in range(0, 100):
        if gender == 'Male':
            gender = 'Female'
        else:
            gender = 'Male'
        first_name, last_name = barnum.create_name()
        email = barnum.create_email(name=(first_name, last_name))
        student = Student(name=first_name + ' ' + last_name, email=email, gender=gender)
        session.add(student)
    session.commit()


# stud_1_pref_1 = Preference(first_name1 = "Lily", last_name1 = "K", student_id = 1, gender = "F", student = student1, preference_id = 44)
# stud_1_pref_2 = Preference(first_name1 = "Joe", last_name1 = "C", student_id = 1, gender = "M", student = student1, preference_id = 7)
# stud_1_pref_3 = Preference(first_name1 = "Irene", last_name1 = "S", student_id = 1, gender = "F", student = student1, preference_id = 66)
def create_preferences():
    students = session.query(Student).all()
    for student in students:
        for i in range(0, 3):
            # grab random student
            random_student = random.choice(students)
            while (random_student.name == student.name and random_student.email == student.email):
                random_student = random.choice(students)

            # set preference
            pref = Preference(name=random_student.name, student_id=student.id, gender=random_student.gender, preference_id=random_student.id)
            session.add(pref)
    session.commit()


create_students()
create_preferences()
