# project/test_basic.py
from flask import Flask, render_template, request, redirect, url_for, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from test_database_setup import Base, Student, engine, Preference
#from test_database_setup import Trip
import os
import unittest
from application import showTrip, showStudent, addStudentsToTrip
from application import session, app
from flask import json


app = Flask(__name__)
engine = create_engine('sqlite:///test_database.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


class BasicTests(unittest.TestCase):

    ############################
    #### setup and teardown ####
    ############################

#     def setUp(self):
#         app.config['TESTING'] = True
#         app.config['WTF_CSRF_ENABLED'] = False
#         app.config['DEBUG'] = False
#         app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test_database.db'
#         self.app = app.test_client()
#
# # executed after each test
#     def tearDown(self):
#         pass

    # executed prior to each test



###############
#### tests ####
###############


    def test_showStudent(self):
        with app.app_context():
<<<<<<< HEAD
            # trip_to_test = session.query(Trip).filter_by(id=1).one()
            # emptyResults = [{ "trip_name" : "Death Valley Backpacking" },
            #         { "id" : 1 },
            #         { "trip_grade" : 9 }, { "trip_students" : None }]
            # results = showTrip(1)
            # self.assertTrue(results,emptyResults)

            student_list = session.query(Student).all()
            more_results = addStudentsToTrip(1,11)
            correct_results = [
              {
                "first_name": "Sammy",
                "grade": 11,
                "last_name": "Levy"
              },
              {
                "first_name": "Serena",
                "grade": 11,
                "last_name": "Hingorani"
              },
              {
                "first_name": "Sammy",
                "grade": 11,
                "last_name": "Bernstein"
              },
              {
                "first_name": "Noah",
                "grade": 11,
                "last_name": "Rizika"
              },
              {
                "first_name": "Wyatt",
                "grade": 11,
                "last_name": "Wagner"
              },
              {
                "first_name": "Dawson",
                "grade": 11,
                "last_name": "Goldsmith"
              },
              {
                "first_name": "Christina",
                "grade": 11,
                "last_name": "Bruni"
              }
            ]
            self.assertEqual(more_results, correct_results)
=======
            expected_results = { "first_name" : "Michael"
                        , "last_name" : "Huang"
                        }
            results = showStudent(1)
            self.assertEqual(results, expected_results)

    # def test_showStudents(self):
    #         expected_results = [{ 'first_name' : 'Michael'
    #                     , 'last_name' : 'Huang'
    #                     }, { 'first_name' : 'J'
    #                                 , 'last_name' : 'D'
    #                                 }]
    #         results = showStudents(session)
    #         self.assertEqual(results, expected_results)

    # def test_showStudentPref(self):
    #         expected_results = [{'name' : 'Michael'},
    #                         {'name' : 'Ryan'},
    #                         {'name' : 'David'}
    #                     ]
    #         results = showStudentPref(2, session)
    #         self.assertEqual(results, expected_results)

    def test_add_students(self):
        with app.app_context():
            expected_results = { "trip_name" : "Death Valley Backpacking" ,
                     "id" : 1,
                    "trip_grade" : 9 }
            results = showTrip(1)
            print(results)
            response_json = json.loads(results[0].data.decode('utf-8'))
            print(response_json)
            self.assertEqual(response_json, expected_results)
>>>>>>> b87c2af15a5701006216835f805a5cffe04386f2

if __name__ == "__main__":
    unittest.main()
