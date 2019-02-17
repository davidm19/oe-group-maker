import json
import random
import string
import flask

from flask import (Flask, flash, jsonify, make_response, redirect,
                   render_template, request)
from flask import session as login_session
from flask import url_for
from flask_cors import CORS
from sqlalchemy import asc, create_engine, desc
from sqlalchemy.orm import sessionmaker

from database_setup import Base, Preference, Student, Trip, engine


app = Flask(__name__)
CORS(app)
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
def show_trips():
    trip_list = []
    all_trips = session.query(Trip).all()
    for trip in all_trips:
        trip_list.append(trip.serialize)
    return flask.jsonify(trip_list), 200


@app.route('/trips/<int:trip_id>/detail', methods=['GET'])
def show_trip(trip_id):
    trip = session.query(Trip).filter_by(id=trip_id).one()
    return flask.jsonify(trip.serialize), 200


@app.route('/trips/new', methods=['POST'])
def add_trip():
    post = request.get_json()
    if request.method == 'POST':
        new_trip = Trip(trip_name=post["trip_name"],
                        trip_grade=post["trip_grade"])
    session.add(new_trip)
    session.commit()
    return flask.jsonify("Trip successfully added!"), 200


@app.route('/trips/<int:id>/update', methods=['PUT'])
def update_trip(id):
    post = request.get_json()
    if "id" not in post:
        return "ERROR: Not a valid Customer ID \n", 404
    trip_id = post["id"]
    edited_trip = session.query(Trip).filter_by(id=trip_id).one()
    if "trip_name" in post:
        edited_trip.trip_name = post["trip_name"]
    session.add(edited_trip)
    session.commit()
    return flask.jsonify("Trip successfully updated! \n"), 200


@app.route('/trips/<int:trip_id>/delete', methods=['DELETE'])
def delete_trip(trip_id):
    trip_to_delete = session.query(Trip).filter_by(id=trip_id).one()
    session.delete(trip_to_delete)
    session.commit()
    return flask.jsonify("Trip successfully deleted!"), 200


""" ====================================== """
""" ====================================== """
""" ====== STUDENfrom flask_cors import CORS
from sqlalchemy import asc, create_engine, desc
from sqlalchemy.orm import sessionmakerT AND TRIP METHODS ====== """
""" ====================================== """
""" ====================================== """


@app.route('/students/gradeLevel/<int:grade>', methods=['GET'])
def get_students_in_grade(grade):
    student_grade_list = []
    students_in_grade = session.query(Student).filter_by(grade=grade).all()
    for student in students_in_grade:
        student_grade_list.append(student.serialize)
    return flask.jsonify(student_grade_list), 200


@app.route('/trips/<int:trip_id>/detail/students', methods=['GET'])
def get_students_in_trip(trip_id):
    trip_student_list = []
    trip = session.query(Trip).filter(Trip.id == trip_id).one_or_none()
    for student in trip.students:
        trip_student_list.append(student.serialize)
    return flask.jsonify(trip_student_list), 200


@app.route('/trips/<int:trip_id>/assignStudentsToTrip', methods=['POST'])
def assign_students_to_trip(trip_id):
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


@app.route('/students/<int:student_id>/', methods=['GET'])
def show_student(student_id):
    student = session.query(Student).filter_by(id=student_id).one()
    return flask.jsonify(student.serialize), 200


@app.route('/students/new', methods=['POST'])
def create_student():
    post = request.get_json()
    if request.method == 'POST':
        new_student = Student(
            first_name=post["first_name"], last_name=post["last_name"])
    session.add(new_student)
    session.commit()
    return flask.jsonify("Student successfully added! \n"), 200


@app.route('/students/<int:student_id>/edit', methods=['PUT'])
def edit_student(student_id):
    post = request.get_json()
    if "id" not in post:
        return "ERROR: Not a valid request \n", 404
    student_id = post["id"]
    edited_student = session.query(Student).filter_by(id=student_id).one()
    if 'first_name' in post:
        edited_student.first_name = post['first_name']
    elif 'last_name' in post:
        edited_student.last_name = post['last_name']
    session.add(edited_student)
    session.commit()
    return flask.jsonify("Student successfully updated! \n"), 200


@app.route('/students/<int:student_id>/delete', methods=['PUT'])
def delete_student(student_id):
    post = request.get_json()
    if "id" not in post:
        return "ERROR: Not a valid request \n", 404
    student_id = post["id"]
    student_to_delete = session.query(Student).filter_by(id=student_id).one()
    session.delete(student_to_delete)
    session.commit()
    return flask.jsonify("Student successfully deleted! \n"), 200


""" ======== STUDENT PREFERENCE CRUD METHODS ======== """


@app.route('/student/<int:student_id>/preferences', methods=['GET'])
def show_student_preferences(student_id):
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
