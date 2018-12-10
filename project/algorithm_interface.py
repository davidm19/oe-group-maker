import flask
from flask import Flask, render_template, request, redirect, jsonify, url_for, flash
from sqlalchemy import create_engine, asc, desc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Student, engine, Preference
from flask import session as login_session
import random, string
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests
from Student import Student_class

DBSession = sessionmaker(bind=engine)
session = DBSession()

'''
selects students from grade level
'''
# def getstudents_by_gradelevel(gradeLevel):
#     return session.query(Student).filter_by(grade=gradeLevel).all()

'''
selects students from trip ID
'''
# def getstudents_by_tripID(tripID):
#     return session.query(Student).filter_by(id = tripID).all()

# def getpreferences_by_studentID(studID):
#     return session.query(Preference).filter_by(id = studID).all()

'''
finds tentative parteners for each person using student ID
'''
def temp_partner_id(student, stuID):
    student.partner = session.query(Preference).filter_by(student_id = stuID.id).all()
    return student.partner

'''
finds tentative parteners for each person using student last name
'''
def temp_partner_last_name(student, stuLN):
    student.partner = session.query(Preference).filter_by(last_name = stuLN).one()
    return student.partner

'''
eliminates partners given a preference string
'''
# def remove_one_student(student, preference):
#     student.remove_preference_string(preference)

'''
eliminates students in a lower preference rating compared to the given
'''
# def remove_lesser_students(student, preference):
#     time_to_delete = False
#     for x in student.preferences:
#         if time_to_delete == True:
#             student.remove_preference_string(preference)
#         if preference == student.prefernces[x]:
#             time_to_delete = True
#
# def setup(num):
#     for x in range(num):
#         students.append(Student())

'''
deletes preferences lower than the "most preferred"... step 2 of the irving algorithm
'''
def remove_lowpriority_pairs(student, session):
#find first preference (student y) of given student (student x)
    # preferences = session.query(Preference).filter_by(student_id = student.id).all()
    preferences = session.query(Preference).filter_by(priority = 3)
    #print(preferences)
    first_priority = preferences.filter_by(student_id = student.id).one()
    student_to_keep = session.query(Student).filter_by(first_name = first_priority.name).one()
    student_tk = Student_class(session.query(Preference).filter_by(student_id = student_to_keep.id).all(), student_to_keep.first_name, student_to_keep.last_name)
#find student x in student y's preference list
    for x in range(len(student_tk.preferences)):
        if student == student_tk.preferences[x]:
            c is 1
            if c > x:
#remove students (z) in student y's preference list that have lower priority than student x
#remove student y from students z's lists
                student_to_be_removed = student_to_keep.preferences[c]
                student_tbr = session.query(Student).filter_by(first_name = student_to_be_removed).one()
                student_remove = Student_class(session.query(Preference).filter_by(student_id = student_tbr.id).all(), student_tbr.first_name, student_tbr.last_name)
                for i in student_remove.preferences:
                    if student_tk.first_name == student_remove.preferences[i]:
                        student_remove.remove_preference_id(i)
                        studs_to_del = session.query(Preference).filter_by(student_id = student_to_keep.id).all()
                        session.remove(studs_to_del.filter_by(name = student_to_keep.first_name).one())
                student_tk.remove_preference_id(c)
                studs_to_remove = session.query(Preference).filter_by(student_id = student_tbr.id)
                studs_to_remove = studs_to_remove.filter_by(name = student_tbr.first_name)
                for stud in studs_to_remove:
                    session.remove(stud)
                c += 1
            else:
                c += 1

#input student is student x
#first_priority is same student as student_to_keep and student_tk (student y)
#student_to_be_removed is same student as student_tbr and student_remove (student z)

# def cycle_finder(students):
#     i = 0;
#     while True:
#         p.append(students[i])
#         q.append(students[i].preferences[-1])
#         i += 1
#
# def check_for_num_pref(student, session):
#     if len(student.preferences) > 2:
#         for preference in student.preferences:
#             stud_pref = session.query(Student).filter_by(first_name = preference).one()
#             remove_pref = session.query(Preference).filter_by(name = student.fn).all()
#             if remove_pref.filter_by(student_id = stud_pref.id).one() is none:
#                 session.remove(preference)



'''
exports the final list (currently returns doubles, this is a bad thing and will be fixed)
'''
def export_list(students, num):
    list = ""
    for x in num:
        list.append(students[x] + ", " + students[x].partner)

    return list

sp1 = ["Bob", "Joe", "Fred"]
s1 = Student(sp1, "Ryan", "Hom")
print(temp_partner_id(s1, 0))
