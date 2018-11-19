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
deletes preferences lower than the "most preferred"... step 2 of the irving algorithm
'''
def remove_lowpriority_pairs(student):
#find first preference (student y) of given student (student x)
    first_priority = student.preferences[0]
    student_to_keep = session.query(Student).filter_by(first_name = first_priority).one()
    student_tk = Student(session.query(Preference).filter_by(student_id = student_to_keep.id).all(), student_to_keep.first_name, student_to_keep.last_name)
#find student x in student y's preference list
    for x in student_tk.preferences:
        if student == studentk.preferences[x]:
            c is 1
            if c > x:
#remove students (z) in student y's preference list that have lower priority than student x
#remove student y from student z's lists
                student_to_be_removed = student_to_keep.preferences[c]
                student_tbr = session.query(Student).filter_by(first_name = student_to_be_removed).one()
                student_remove = Student(session.query(Preference).filter_by(student_id = student_tbr.id).all(), student_tbr.first_name, student_tbr.last_name)
                for i in student_remove.preferences:
                    if student_tk.first_name == student_remove.preferences[i]:
                        student_remove.remove_preference_id(i)
                student_tk.remove_preference_id(c)
                c += 1
            else:
                c += 1

#input student is student x
#first_priority is same student as student_to_keep (student y)
#student_to_be_removed is same student as student_tbr (student z)


'''
exports the final list (currently returns doubles, this is a bad thing and will be fixed)
'''
def export_list(students, num):
    list = ""
    for x in num:
        list.append(students[x] + ", " + students[x].partner)

    return list

print(getstudents_by_gradelevel(0))
