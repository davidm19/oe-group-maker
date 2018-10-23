import flask
from flask import Flask, request
from sqlalchemy import create_engine, asc, desc
from sqlalchemy.orm import sessionmaker
from collections import defaultdict
import application
from database_setup import Base, Student, PreferredMember

engine = create_engine('sqlite:///database.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

def getStudentList():
    session = DBSession()
    students = session.query(Student).all()
    for student in students:
        student_list = student
    return student_list

def getStudent():
    session = DBSession()
    student = session.query(Student).filter_by(id=ID).one()
    return student

def getPreferred():
    session = DBSession()
    preferred = session.query(PreferredMember).all()
    return preferred

def splitStudents(students):
    students = getStudents()
    half = len(students)/2
    return students[:half], students[half:]

def makeDicts(student, preferred):
    studentDict = dict()
    students = getStudentList()
    for i in students:
        dict(i) = student, preferred
    return studentDict

'''
make dictionnaries (student, [who they prefer])
'''
