# project/test_basic.py
from flask import Flask, render_template, request, redirect, url_for, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from test_database_setup import Base, Student, engine, Preference
import os
import unittest
from application import showStudent, showStudents, showStudentPref, newStudent
from application import session, app


app = Flask(__name__)
engine = create_engine('sqlite:///test_database.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


class BasicTests(unittest.TestCase):


    def test_showStudent(self):
        expected_results = { "first_name" : "Michael"
                    , "last_name" : "Huang"
                    }
        results = showStudent(1, session)
        self.assertEqual(results, expected_results)

    def test_temp_partner(self):
        expected_results = {
        }
        results = temp_partner()
        self.assertEqual()

    def test_remove_one_student(self):
        expected_results = {}
        results = remove_one_student()
        self.assertEqual()

if __name__ == "__main__":
    unittest.main()
