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
from flask_cors import CORS



app = Flask(__name__)
CORS(app)

# cors = CORS(app, resources={r"/api/*": {"origins": "*"}})



# CLIENT_ID = json.loads(open('client_secrets.json', 'r').read())['web']['client_id']
APPLICATION_NAME = "Outdoor Ed Group Maker"

engine = create_engine('sqlite:///database.db?check_same_thread=false')
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
    tripList = []
    allTrips = session.query(Trip).all()
    for trip in allTrips:
        tripList.append(trip.serialize)
    return flask.jsonify(tripList), 200

@app.route('/trips/<int:trip_id>/detail', methods=['GET'])
def showTrip(trip_id):
    trip = session.query(Trip).filter_by(id=trip_id).one()
    return flask.jsonify(trip.serialize), 200


@app.route('/trips/new', methods=['POST'])
def addTrip():
    post = request.get_json()
    if request.method == 'POST':
        newTrip = Trip(trip_name = post["trip_name"],
                        trip_grade = post["trip_grade"])
    session.add(newTrip)
    session.commit()
    return flask.jsonify("Trip successfully added!"), 200

@app.route('/trips/<int:id>/update', methods=['PUT'])
def updateTrip(id):
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

@app.route('/trips/<int:trip_id>/delete', methods=['DELETE'])
def deleteTrip(trip_id):
    tripToDelete = session.query(Trip).filter_by(id = trip_id).one()
    session.delete(tripToDelete)
    session.commit()

    return flask.jsonify("Trip successfully deleted!"), 200


""" ====================================== """
""" ====================================== """
""" ====== STUDENT AND TRIP METHODS ====== """
""" ====================================== """
""" ====================================== """
@app.route('/students/gradeLevel/<int:grade>', methods=['GET'])
def getStudentsInGrade(grade):
    studentGradeList = []
    studentsInGrade = session.query(Student).filter_by(grade=grade).all()
    for student in studentsInGrade:
        studentGradeList.append(student.serialize)
    return flask.jsonify(studentGradeList), 200

@app.route('/trips/<int:trip_id>/detail/students',methods=['GET'])
def getStudentsInTrip(trip_id):
    tripStudentList = []
    trip = session.query(Trip).filter(Trip.id == trip_id).one_or_none()
    for student in trip.students:
        tripStudentList.append(student.serialize)
    return flask.jsonify(tripStudentList), 200

@app.route('/trips/<int:trip_id>/assignStudentsToTrip', methods=['POST'])
def assignStudentsToTrip(trip_id):
    student_assign_list = []
    student_ids = request.get_json()
    for s_id in student_ids:
        student = session.query(Student).filter(Student.id == s_id).one()
        student_assign_list.append(student)

    trip = session.query(Trip).filter(Trip.id == trip_id).one()
    trip.students = student_assign_list
    session.add(trip)
    session.commit()
    return flask.jsonify("Success"), 200


""" ======================================= """
""" ======================================= """
""" === END OF STUDENT AND TRIP METHODS === """
""" ======================================= """
""" ======================================= """
#
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

#METHODS WITH TRIPTHING

# @app.route('/trips/<int:trip_id>/students', methods=['GET'])
# def showStudents(trip_id):
#     session = DBSession()
#     students = session.query(Student).all()
#     students_all = list()
#     for student in students:
#         student_info = { "first_name" : student.first_name
#                     , "last_name" : student.last_name
#                     , "grade" : student.grade
#                     }
#         students_all.append(student_info)
#     return flask.jsonify(students_all), 200

# @app.route('/trips/<int:trip_id>/students/<int:ID>/', methods=['GET'])
# def showStudent(trip_id, ID, GRADE):
#     session = DBSession()
#     student = session.query(Student).filter_by(id=ID).one()
#     student_info = { "first_name" : student.first_name
#                 , "last_name" : student.last_name
#                 , "grade" : student.grade
#                 }
#     return flask.jsonify(student_info), 200

# @app.route('/trips/<int:trip_id>/students/new', methods=['POST'])
# def newStudent(trip_id):
#     session = DBSession()
#     post = request.get_json()
#     if request.method == 'POST':
#         newStudent = Student(first_name = post["first_name"], last_name = post["last_name"], grade = post["grade"])
#     session.add(newStudent)
#     session.commit()
#     return flask.jsonify("Student successfully added! \n"), 200

# @app.route('/trips/<int:trip_id>/students/<int:id>/edit', methods=['PUT'])
# def editStudent(trip_id, id):
#     session = DBSession()
#     post = request.get_json()
#     if "id" not in post:
#         return "ERROR: Not a valid Customer ID \n", 404
#     student_id = post["id"]
#     editedStudent = session.query(Student).filter_by(id=student_id).one()
#     if 'first_name' in post:
#         editedStudent.first_name = post['first_name']
#     elif 'last_name' in post:
#         editedStudent.last_name = post['last_name']
#     elif 'grade' in post:
#         editedStudent.grade = post['grade']
#     session.add(editedStudent)
#     session.commit()
#     return flask.jsonify("Student successfully updated! \n"), 200

# @app.route('/trips/<int:trip_id>/students/<int:id>/delete', methods=['PUT'])
# def deleteStudent(trip_id, id):
#     session = DBSession()
#     post = request.get_json()
#     if "id" not in post:
#         return "ERROR: Not a valid Customer ID \n", 404
#     student_id = post["id"]
#     studentToDelete = session.query(Student).filter_by(id=id).one()
#     session.delete(studentToDelete)
#     session.commit()
#     return flask.jsonify("Student successfully deleted! \n"), 200

""" ======== STUDENT PREFERENCE CRUD METHODS ======== """
@app.route('/student/<int:student_id>/preferences', methods=['GET'])
def show_student_preferences(student_id):
    session = DBSession()
    student = session.query(Student).filter(Student.id == student_id).one()
    preferences_all = []
    for preference in student.preferences:
        print(preference)
        preferences_all.append(preference.serialize)
    return flask.jsonify(preferences_all), 200

@app.route('/student/<int:student_id>/assignPreferencesToStudent', methods=['POST'])
def assign_preferences_to_student(student_id):
    new_preferences = []
    preference_ids = request.get_json()
    for p_id in preference_ids:
        student = session.query(Student).filter(Student.id == p_id).one()
        new_preferences.append(student)

    student = session.query(Student).filter(Student.id == student_id).one()
    student.preferences = new_preferences
    session.add(student)
    session.commit()
    return flask.jsonify("Success"), 200


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
