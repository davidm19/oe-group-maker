from flask import Flask, render_template, request, redirect, url_for, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from test_database_setup import Base, Student, engine, Preference
import os
import unittest
from application import showStudent, showStudents, showStudentPref, newStudent
from application import session, app
from algorithm_interface import remove_lowpriority_pairs
from Student import student


app = Flask(__name__)
engine = create_engine('sqlite:///testalg_database.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


class BasicTests(unittest.TestCase):

    def test_stepTwo(self):
        newStudent(Char, Lie, Paul, Sam, Kel, session)
        newStudent(Pete, R, Kel, Sam, Paul, session)
        newStudent(Eli, S, Sam, Kel, Paul, session)
        newStudent(Paul, Ly, Eli, Char, Sam, session)
        newStudent(Kel, Ly, Pete, Char, Sam, session)
        newStudent(Sam, My, Char, Paul, Eli, session)
        students = session.query(Student).all()
        for student in students:
            remove_lowpriority_pairs(student, session)
        expected_results = {{Char, Lie, Paul, Sam}, {Pete, R, Kel},{Eli,S, Sam, Paul}, {Paul,Ly, Eli, Char}, {Kel, Ly, Pete}, {Sam, My, Char, Eli}}
        results = {}
