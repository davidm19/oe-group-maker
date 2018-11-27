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

# CLIENT_ID = json.loads(open('client_secrets.json', 'r').read())['web']['client_id']
APPLICATION_NAME = "Outdoor Ed Group Maker"

engine = create_engine('sqlite:///database.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()




@app.route('/trips', methods=['GET'])
def showTrips():
    tripList = []
    allTrips = session.query(Trip).all()
    for trip in allTrips:
        trip_info = {"trip_name" : trip.trip_name, "id" : trip.id}

        tripList.append(trip_info)

    return flask.jsonify(tripList), 200



@app.route('/trips', methods=['GET', 'POST'])
def addTrip():
    tripList = []
    if request.method == 'POST':
        newTrip = Trip(trip_name = request.form['trip_name'])
        session.add(newTrip)
        session.commit()
        tripList.append(newTrip)

    return flask.jsonify("Trip Added!"), 200

@app.route('/trips/<int:trip_id>/delete', methods=['GET, POST'])
def deleteTrip():
    tripList = []
    tripToDelete = session.query(Trip).filter_by(id=trip_id).one()
    if request.method == 'POST':
        session.delete(tripToDelete)
        session.commit()
        tripList.remove(tripToDelete)

    return flask.jsonify("Trip Deleted!"), 200

@app.route('/student/<int:ID>/')
def showStudent(ID, session):
    student = session.query(Student).filter_by(id=ID).one()
    student_info = { "first_name" : student.first_name
                , "last_name" : student.last_name
                }
    return student_info

def newTrip():
    pass
    #SAME AS NEWUNIVERSE IN ITEM CATALOG?
    """TODO: IMPLEMENT"""

@app.route('/student/<int:ID>')
def showStudentPref(ID, session):
    preferences = session.query(Preference).filter_by(student_id=ID).all()
    preferences_all = list()
    for preference in preferences:
        preference_name = { "name" : preference.name}
        preferences_all.append(preference_name)
    return preferences_all

@app.route('/students')
def showStudents(sesh):
    students = sesh.query(Student).all()
    students_all = list()
    for student in students:
        student_info = { "first_name" : student.first_name
                    , "last_name" : student.last_name
                    }
        students_all.append(student_info)
    return students_all

@app.route('/student/new/', methods=['GET', 'POST'])
def newStudent(firstName, lastName, pref1_name, pref2_name, pref3_name, sesh):
    if request.method == 'POST':
        students = sesh.query(Student).all()
        newStudent = Student(first_name = firstName, last_name = lastName)
        sesh.add(newStudent)
        sesh.commit()
        if pref1_name is not none:
            student_pref1 = Preference(name = pref1_name, priority = 3, student_id = newStudent.id)
            sesh.add(student_pref1)
            sesh.commit()
        if pref2_name is not none:
            student_pref2 = Preference(name = pref2_name, priority = 2, student_id = newStudent.id)
            sesh.add(student_pref2)
            sesh.commit()
        if pref3_name is not none:
            student_pref3 = Preference(name = pref1_name, priority = 1, student_id = newStudent.id)
            sesh.add(student_pref3)
            sesh.commit()
        return "yes" #RETURN REDIRECT URLFOR FOR HOMEPAGE???
    else:
        return "no" #RETURN RENDERTEMPLATE FOR NEWSTUDENT??? (KINDA LIKE ITEM CATALOG NEW CHARACTER)

@app.route('/student/<int:ID>/edit', methods=['GET', 'POST'])
def editStudent(ID):
    session = DBSession()
    editedStudent = session.query(Student).filter_by(id=ID).one()
    if request.method == 'POST':
        if request.form['first_name']:
            editedStudent.first_name = request.form['first_name']
        session.add(editedStudent)
        session.commit()
        return redirect(url_for('showStudents', id=ID))
    else:
        return flask.jsonify("it worked"), 200
        # return render_template('editUniverse.html', universe=editedUniverse)

@app.route('/student/<int:ID>/delete', methods=['GET', 'POST'])
def deleteStudent(ID):
    session = DBSession()
    studentToDelete = session.query(Student).filter_by(id=ID).one()
    prefs_delete = session.query(Preference).filter_by(student_id = ID).all()
    if request.method == 'POST':
        session.delete(studentToDelete)
        for pref in pres_delete:
            session.delete(pref)
        session.commit()
        return redirect(url_for('showStudents', id=ID))
    else:
        return "it worked"
        # return render_template('deleteUniverse.html', universe=universeToDelete)

if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
