import flask
from flask import Flask, render_template, request, redirect
from flask import jsonify, url_for, flash
from sqlalchemy import create_engine, asc, desc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Student, engine, Preference
from flask import session as login_session
import random
import string
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests
from Student_class import Student_class

app = Flask(__name__)
engine = create_engine('sqlite:///database.db')
Base.metadata.bind = engine
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


def temp_partner_id_db(student, stuID):
    student.partner = session.query(Preference).filter_by(student_id=stuID)
    .filter_by(priority=1).one().name
    return student.partner


'''
finds tentative parteners for each person using student preference list
'''


def temp_partner_id(student):
    if (student.preference_index >= len(student.preferences)):
        student.partner = Preference(name='NO MATCH')
    else:
        student.partner = student.preferences[student.preference_index]
        student.preference_index = student.preference_index + 1

    return student.partner


def remove_extraneous_preferences(student):
    i = 1
    while i < student.preference_index:
        student.remove_preference_id(i)
        i += 1


'''
finds tentative parteners for each person using student last name
'''


def temp_partner_last_name(student, stuLN):
    student.partner = session.query(Preference).
    filter_by(last_name=stuLN).one().name
    return student.partner


'''
eliminates partners given a preference string
'''

'''
deletes preferences lower than the "most preferred"
step 2 of the irving algorithm
'''


def remove_lowpriority_pairs(student, session):
    preferences = session.query(Preference).filter_by(priority=5)
    first_priority = preferences.filter_by(student_id=student.id).one()
    student_to_keep = session.query(Student)
    .filter_by(first_name=first_priority.name).one()
    student_tkPrefs = session.query(Preference).
    filter_by(student_id=student_to_keep.id).all()
    for stud in student_tkPrefs:
        print(stud.name)
    student_tk = Student_class(student_tkPrefs,
                               student_to_keep.first_name,
                               student_to_keep.last_name)
# find student x in student y's preference list
    x = 0
    i = len(student_tkPrefs)
    for stud in student_tk.preferences:
        x += 1
        if student.first_name == stud.name:
            k = stud.priority
            while(x < i + 1):
                k = k - 1
                preference_to_del = session.query(Preference)
                .filter_by(student_id=student_to_keep.id)
                if preference_to_del
                .filter_by(priority=k).one_or_none() is not None:
                    preference = preference_to_del.filter_by(priority=k).one()
                    session.delete(preference)
                    id_pref_to_del = preference.id
                    name_of_pref = preference.name
# remove students (z) in student y's preference
# list that have lower priority than student x
# remove student y from students z's lists
                    student_tbr = session.query(Student)
                    .filter_by(first_name=name_of_pref).one()
                    student_remove = Student_class(session.query(Preference)
                                                   .filter_by(
                                                   student_id=student_tbr.id)
                                                   .all(),
                                                   student_tbr.first_name,
                                                   student_tbr.last_name
                                                   )
                    for stud in student_remove.preferences:
                        if stud.name == student_to_keep.first_name:
                            studs_to_del = session.query(Preference)
                            .filter_by(name=student_to_keep.first_name)
                            if studs_to_del
                            .filter_by(student_id=student_tbr.id).one_or_none()
                            is not None:
                                studs_to_del = studs_to_del
                                .filter_by(student_id=student_tbr.id).one()
                                session.delete(studs_to_del)
                                session.commit()
                x += 1


def export_list(students):
    list = []
    for x in students:
        list.append("%s --- %s" % (x.first_name, x.partner.name))

    return list


def export_list_preferences(students):
    list = []
    student_pref = ""
    for x in students:
        student_pref = x.first_name + " --- "
        for i in range(len(x.preferences)):
            student_pref = student_pref + "%s, " % (x.preferences[i].name)
        list.append(student_pref)

    return list


'''sp1 = ["Bob", "Joe", "Fred"]
sp2 = session.query(Preference).filter_by(student_id = 2).all()
sp3 = []
for i in sp2:
    sp3.append(i.name)
s1 = Student_class(sp3, "Ryan", "Hom")
print(temp_partner_id(s1))

print(sp3)'''

'''
Janky first step in the alg. Will put into a method
'''


def step_one(self, session):

    students = []
    temp1 = session.query(Student).all()
    temp2 = None
    temp3 = []
    count = 1
# makes a list of Student objects from the database
    for i in temp1:
        temp2 = session.query(Preference).filter_by(student_id=count).all()
        students.append(Student_class(temp2, i.first_name, i.last_name))
        count = count + 1
    same = 0
    exit_loop = False
    iterstudents = iter(students)
    next(iterstudents)
    while same < 1:
        for i in students:
            if(i.partner == ""):
                temp_partner_id(i).name
        for i in students:
            for x in iterstudents:
                if(type(x.partner) is Preference):
                    if(i.partner.name == x.partner.name):
                        for y in students:
                            if(i.partner.name == y.first_name):
                                for a in range(len(y.preferences) - 1, 0, -1):
                                    if(y.preferences[a].name == i.first_name):
                                        temp_partner_id(i).name
                                        y.remove_preference_string(
                                            y.preferences[a])
                                        exit_loop = True
                                    elif(y.preferences[a].name
                                         == x.first_name):
                                        temp_partner_id(x).name
                                        y.remove_preference_string(
                                            y.preferences[a])
                                        exit_loop = True
                                if(exit_loop is True):
                                    exit_loop = False
                                    break
        for y in students:
            remove_extraneous_preferences(y)
        same += 1


print(export_list(students))
print(export_list_preferences(students))
