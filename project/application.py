import flask
from flask import Flask, render_template, request, redirect, jsonify, url_for, flash
from sqlalchemy import create_engine, asc, desc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Student, engine, Preference, Trip
#from database_setup import Trip
from flask import session as login_session
import random, string
import json
from flask import make_response
from sqlalchemy.sql import exists
#from flask_cors import CORS



app = Flask(__name__)
#CORS(app)

# CLIENT_ID = json.loads(open('client_secrets.json', 'r').read())['web']['client_id']
APPLICATION_NAME = "Outdoor Ed Group Maker"

engine = create_engine('sqlite:///database.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


""" ======== TRIP CRUD METHODS ======== """

@app.route('/trips', methods=['GET'])
def showTrips():
    session = DBSession()
    tripList = []
    allTrips = session.query(Trip).all()
    # trip_id = request.args.get('trip_id')
    # trip_name = request.args.get('trip_name')
    for trip in allTrips:
        trip_info = {"trip_name" : trip.trip_name, "id" : trip.id}
        tripList.append(trip_info)
    return flask.jsonify(tripList), 200

@app.route('/trips/<int:ID>/', methods=['GET'])
def showTrip(ID):
    session = DBSession()
    trip = session.query(Trip).filter_by(id=ID).one()
    trip_info = { "trip_name" : trip.trip_name, "id" : trip.id }
    return flask.jsonify(trip_info), 200

@app.route('/trips/new', methods=['POST'])
def addTrip():
    session = DBSession()
    post = request.get_json()
    if request.method == 'POST':
        newTrip = Trip(trip_name = post["trip_name"])
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
    editedTrip = session.query(Trip).filter_by(id = trip_id).one()
    if "trip_name" in post:
        editedTrip.trip_name = post["trip_name"]
    session.add(editedTrip)
    session.commit()
    return flask.jsonify("Trip successfully updated! \n"), 200

@app.route('/trips/<int:id>/delete', methods=['PUT'])
def deleteTrip(id):
    session = DBSession()
    post = request.get_json()
    if "id" not in post:
        return "ERROR: Not a valid Customer ID \n", 404
    trip_id = post["id"]
    tripToDelete = session.query(Trip).filter_by(id=id).one()
    session.delete(tripToDelete)
    session.commit()

    return flask.jsonify("Trip successfully deleted!"), 200

""" ======== STUDENT CRUD METHODS ======== """

@app.route('/students', methods=['GET'])
def showStudents():
    session = DBSession()
    students = session.query(Student).all()
    students_all = list()
    for student in students:
        student_info = { "first_name" : student.first_name
                    , "last_name" : student.last_name
                    }
        students_all.append(student_info)
    return flask.jsonify(students_all), 200

@app.route('/students/<int:ID>/', methods=['GET'])
def showStudent(ID):
    session = DBSession()
    student = session.query(Student).filter_by(id=ID).one()
    student_info = { "first_name" : student.first_name
                , "last_name" : student.last_name
                }
    return flask.jsonify(student_info), 200

#NEED SHOW STUDENT + PREFS METHODS NOW!!

@app.route('/students/new', methods=['POST'])
def newStudent():
    session = DBSession()
    post = request.get_json()
    if request.method == 'POST':
        newStudent = Student(first_name = post["first_name"], last_name = post["last_name"])
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
        preference_name = { "name" : preference.name}
        preferences_all.append(preference_name)
    return flask.jsonify(preferences_all), 200


@app.route('/student/<int:ID>/prefs', methods=['GET'])
def showStudentPref(ID):
    session = DBSession()
    preferences = session.query(Preference).filter_by(student_id=ID).all()
    preferences_all = []
    for preference in preferences:
        preference_name = { "name" : preference.name}
        preferences_all.append(preference_name)
    return flask.jsonify(preferences_all), 200

# @app.route('/student/<int:ID>/prefs', methods=['POST'])
# def updateStudentPref()

if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=8000)