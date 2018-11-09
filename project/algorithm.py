import flask
from flask import Flask, request
from sqlalchemy import create_engine, asc, desc
from sqlalchemy.orm import sessionmaker
from collections import defaultdict
from database_setup import Base, Student, PreferredMember

engine = create_engine('sqlite:///database.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

def getStudents():
    session = DBSession()
    students = session.query(Student).all()
    for student in students:
        student_list = student
    return student_list

def splitStudents():
    students = getStudents()
    half = len(students)/2
    return students[:half], students[half:]
    '''
    def split_list(a_list):
        half = len(a_list)//2
        return a_list[:half], a_list[half:]

    A = [1,2,3,4,5,6]
    B, C = split_list(A)
    '''

'''TODO: IMPLEMENT'''
def returnRanking(half1, half2):
    halves = [half1, half2] #RIGHT WAY TO DO THINGS???
    for half in halves:
        for g1member, preferred in half.items():
            for i, g2member in enumerate(preferred):
                return '''TODO: IMPLEMENT'''

'''TODO: IMPLEMENT'''
def prefers():
    #DEPENDS ON RETURNRANKING
    return '''TODO: IMPLEMENT'''

'''TODO: IMPLEMENT'''
def after():
    return '''TODO: IMPLEMENT'''

'''TODO: IMPLEMENT'''
def match():
    return '''TODO: IMPLEMENT'''

'''TODO: IMPLEMENT'''
def checkStable():
    return '''TODO: IMPLEMENT'''
