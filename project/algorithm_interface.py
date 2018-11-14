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
    return session.query(Trip).filter_by(id=tripID).all()

'''
finds tentative parteners for each person
'''
def temp_partner(studentID):
    return session.query(Preference).filter_by(student_id = studentID).one()

'''
eliminates partners given a preference string
'''
def removal_one_student(student, preference):
    student.remove_preference_string(preference)

def remove_lesser_students(student, preference):
    time_to_delete = False
    for x in student.preferences:
        if preference = student.preferences[x]


'''
exports the final list
'''
def export_list():
    pass
