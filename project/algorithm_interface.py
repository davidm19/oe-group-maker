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

ALGORITHM INTERFACE
1. select trip from database
2. algorithm step 1
3. algorithm step 2
4. algorithm step 3
5. export list in some format

'''

'''
selects students from grade level
'''
def getstudents_by_gradelevel(gradeLevel):
    return session.query(Student).filter_by(grade=gradeLevel).all()

'''
selects students from trip ID
'''
def getstudents_by_tripID(tripID):
    return session.query(Student).filter_by(id = tripID).all()

def getpreferences_by_studentID(studID):
    return session.query(Preference).filter_by(id = studID).all()

'''
finds tentative parteners for each person
'''
def temp_partner_id(student, stuID):
    student.partner = session.query(Preference).filter_by(student_id = stuID).one()

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
        if time_to_delete == True:
            student.remove_preference_string(preference)
        if preference == student.prefernces[x]:
            time_to_delete = True

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
