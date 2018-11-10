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
def temp_partner(stuID):
    return session.query(Preference).filter_by(student_id=stuID).all()

'''
eliminates parteners for anyone less than first preference that's a match
'''
def lowpref_removal():
    student1 = session.query(Student)filter_by(student_id=stuID).one()

    pass

'''
part 1 of the algorithm
'''
def alg_part1():
    pass

'''
part 2 of algorithm
'''
def alg_part2():
    pass

'''
part 3 of algorithm
'''
def alg_part3():
    pass

'''
exports the final list
'''
def export_list():
    pass
