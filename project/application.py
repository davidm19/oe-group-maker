import flask
from flask import Flask, render_template, request, redirect, jsonify, url_for
from flask import flash
from sqlalchemy import create_engine, asc, desc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Student, engine, Preference, Trip
# from database_setup import Trip
from flask import session as login_session
import random
import string
import json
from flask import make_response
from sqlalchemy.sql import exists
import os
# from flask_cors import CORS

app = Flask(__name__)
# CORS(app)
# cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

# CLIENT_ID = json.loads(open('client_secrets.json', 'r')
#   .read())['web']['client_id']
APPLICATION_NAME = "Outdoor Ed Group Maker"

SQLALCHEMY_DATABASE_URI = os.environ['DB_URL']
# engine = create_engine('sqlite:///test.db')
engine = create_engine('sqlite:///SQLALCHEMY_DATABASE_URI.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

""" ===================================== """
""" ===================================== """
""" ========= TRIP CRUD METHODS ========= """
""" ===================================== """
""" ===================================== """


@app.route('/trips', methods=['GET'])
def showTrips():
    session = DBSession()
    tripList = []
    allTrips = session.query(Trip).all()
    # trip_id = request.args.get('trip_id')
    # trip_name = request.args.get('trip_name')
    for trip in allTrips:
        trip_info = {"trip_name": trip.trip_name,
                     "id": trip.id,
                     "trip_grade": trip.trip_grade,
                     "trip_students": trip.students}
        tripList.append(trip_info)
    return flask.jsonify(tripList), 200


@app.route('/trips/<int:trip_id>/detail', methods=['GET'])
def showTrip(trip_id):
    session = DBSession()
    # studentList = []
    trip = session.query(Trip).filter_by(id=trip_id).one()
    # students = session.query(Student).filter_by(trip_id=trip_id).all()
    trip_info = {"trip_name": trip.trip_name,
                 "id": trip.id,
                 "trip_grade": trip.trip_grade}
    return flask.jsonify(trip_info), 200


@app.route('/trips/new', methods=['POST'])
def addTrip():
    session = DBSession()
    post = request.get_json()
    if request.method == 'POST':
        newTrip = Trip(trip_name=post["trip_name"],
                       trip_grade=post["trip_grade"])
    session.add(newTrip)
    session.commit()
    return flask.jsonify("Trip successfully added!"), 200


@app.route('/trips/<int:id>/update', methods=['PUT'])
def updateTrip(id):
    session = DBSession()
    post = request.get_json()
    if "id" not in post:
        return "ERROR: Not a valid Customer ID \n", 404
    trip_id = post["id"]
    editedTrip = session.query(Trip).filter_by(id=trip_id).one()
    if "trip_name" in post:
        editedTrip.trip_name = post["trip_name"]
    session.add(editedTrip)
    session.commit()
    return flask.jsonify("Trip successfully updated! \n"), 200


@app.route('/trips/<int:trip_id>/delete', methods=['DELETE'])
def deleteTrip(trip_id):
    print("Deleting trip")
    session = DBSession()
    print("Request is ")
    print(request)
    post = request.get_json()
    print("Post is ")
    print(post)
    print("Trip id is")
    print(trip_id)
    tripToDelete = session.query(Trip).filter_by(id=trip_id).one()
    session.delete(tripToDelete)
    session.commit()
    return flask.jsonify("Trip successfully deleted!"), 200


@app.route('/trips/<int:trip_id>/addGrade', methods=['POST'])
def addGradeToTrip(trip_id, grade):
    session = DBSession()
    tripStudentList = []
    # post = request.get_json()
    studentsInGrade = session.query(Student).filter_by(grade=grade).all()
    trip = session.query(Trip).filter_by(id=trip_id).one()
    if grade is trip_grade:
        for student in studentsInGrade:
            student_info = {"first_name": student.first_name,
                            "last_name": student.last_name}
            tripStudentList.append(student_info)
        return flask.jsonify(tripStudentList)


@app.route('/trips/<int:trip_id>/addStudents', methods=['PUT'])
def assignStudentsToTrip(trip_id, student_list):
    session = DBSession()
    # tripStudentList = []
    trip = session.query(Trip).filter_by(id=trip_id).one()
    trip.students = student_list
    # for student in student_list:
    #    student_info = {"first_name": student.first_name,
    #                    "last_name": student.last_name}
    #    tripStudentList.append(student_info)
    session.add(trip)
    session.commit()
    return "Students successfully added!", 202
    return flask.jsonify(tripStudentList)


""" ====================================== """
""" ====================================== """
""" ======== STUDENT CRUD METHODS ======== """
"""Show trip should be the same thing as showStudents"""
# @app.route('/trips/<int:trip_id>/detail/students', methods=['GET'])
# def showStudents(trip_id):
#     session = DBSession()
#     studentList = []
#     trip = session.query(Trip).filter_by(id=trip_id).one()
#     students = session.query(Student).filter_by(trip_id=trip_id).all()
#     for student in students:
#         student_info = { "first_name" : student.first_name
#                     , "last_name" : student.last_name,
#                     "grade" : student.grade
#                     }
#         studentList.append(student_info)
#     return flask.jsonify(studentList), 200


@app.route('/students/<int:ID>/', methods=['GET'])
def showStudent(ID):
    session = DBSession()
    student = session.query(Student).filter_by(id=ID).one()
    student_info = {"first_name": student.first_name,
                    "last_name": student.last_name}
    return flask.jsonify(student_info), 200

# NEED SHOW STUDENT + PREFS METHODS NOW!!


@app.route('/students/new', methods=['POST'])
def newStudent():
    session = DBSession()
    post = request.get_json()
    if request.method == 'POST':
        newStudent = Student(first_name=post["first_name"],
                             last_name=post["last_name"])
    session.add(newStudent)
    session.commit()
    return flask.jsonify("Student successfully added! \n"), 200


@app.route('/students/<int:id>/edit', methods=['PUT'])
def editStudent(id):
    session = DBSession()
    post = request.get_json()
    if "id" not in post:
        return "ERROR: Not a valid Customer ID \n", 404
    student_id = post["id"]
    editedStudent = session.query(Student).filter_by(id=student_id).one()
    if 'first_name' in post:
        editedStudent.first_name = post['first_name']
    elif 'last_name' in post:
        editedStudent.last_name = post['last_name']
    session.add(editedStudent)
    session.commit()
    return flask.jsonify("Student successfully updated! \n"), 200


@app.route('/students/<int:id>/delete', methods=['PUT'])
def deleteStudent(id):
    session = DBSession()
    post = request.get_json()
    if "id" not in post:
        return "ERROR: Not a valid Customer ID \n", 404
    student_id = post["id"]
    studentToDelete = session.query(Student).filter_by(id=id).one()
    session.delete(studentToDelete)
    session.commit()
    return flask.jsonify("Student successfully deleted! \n"), 200


""" ======== STUDENT PREFERENCE CRUD METHODS ======== """


@app.route('/student/prefs', methods=['GET'])
def showStudentPrefs():
    session = DBSession()
    preferences_all = []
    preferences = session.query(Preference).all()
    for preference in preferences:
        preference_name = {"name": preference.name}
        preferences_all.append(preference_name)
    return flask.jsonify(preferences_all), 200


@app.route('/student/<int:ID>/prefs', methods=['GET'])
def showStudentPref(ID):
    session = DBSession()
    preferences = session.query(Preference).filter_by(student_id=ID).all()
    preferences_all = []
    for preference in preferences:
        preference_name = {"name": preference.name}
        preferences_all.append(preference_name)
    return flask.jsonify(preferences_all), 200


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
