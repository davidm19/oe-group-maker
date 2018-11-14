import flask
from flask import Flask, render_template, request, redirect, jsonify, url_for, flash
from sqlalchemy import create_engine, asc, desc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Student, engine, Preference, Trip
from flask import session as login_session
import random, string
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests
from Student import Student

DBSession = sessionmaker(bind=engine)
session = DBSession()

'''
selects students from grade level
'''
def getstudents_by_gradelevel(gradeLevel):
    return session.query(Student).filter_by(grade=gradeLevel).all()

'''
selects students from trip ID
'''
def getstudents_by_tripID(tripID):
<<<<<<< HEAD
    return session.query(Trip).filter_by(id=tripID).all()
=======
    return session.query(Student).filter_by(id = tripID).all()

def getpreferences_by_studentID(studID):
    return session.query(Preference).filter_by(id = studID).all()
>>>>>>> a250bc65ce361a670485a54503c7d1eeec2fa2fd

'''
finds tentative parteners for each person
'''
<<<<<<< HEAD
def temp_partner(studentID):
    return session.query(Preference).filter_by(student_id = studentID).one()
=======
def temp_partner_id(student, stuID):
    student.partner = session.query(Preference).filter_by(student_id = stuID).one()
>>>>>>> a250bc65ce361a670485a54503c7d1eeec2fa2fd

'''
eliminates partners given a preference string
'''
def remove_one_student(student, preference):
    student.remove_preference_string(preference)

'''
eliminates students in a lower preference rating compared to the given
'''
def remove_lesser_students(student, preference):
    time_to_delete = False
    for x in student.preferences:
<<<<<<< HEAD
        if preference = student.preferences[x]
=======
        if time_to_delete == True:
            student.remove_preference_string(preference)
        if preference == student.prefernces[x]:
            time_to_delete = True
>>>>>>> a250bc65ce361a670485a54503c7d1eeec2fa2fd

def setup(num):
    for x in range(num):
        students.append(Student())

'''
exports the final list (currently returns doubles, this is a bad thing and will be fixed)
'''
def export_list(students, num):
    list = ""
    for x in num:
        list.append(students[x] + ", " + students[x].partner)

    return list

print(getstudents_by_gradelevel(0))
