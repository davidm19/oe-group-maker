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


app = Flask(__name__)
engine = create_engine('sqlite:///database.db')
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

if __name__ == "__main__":
    unittest.main()
