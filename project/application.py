import flask
from flask import Flask, render_template, request, redirect, jsonify, url_for, flash
from sqlalchemy import create_engine, asc, desc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Student, engine, Preference
#from database_setup import Trip
from flask import session as login_session
import random, string
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests


app = Flask(__name__)

# CLIENT_ID = json.loads(open('client_secrets.json', 'r').read())['web']['client_id']
APPLICATION_NAME = "Outdoor Ed Group Maker"

engine = create_engine('sqlite:///database.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/login')
def showLogin():
    state = ''.join(random.choice(string.ascii_uppercase + string.digits)
        for x in xrange(32))
    login_session['state'] = state
    return render_template('login.html', STATE=state)

@app.route('/gconnect', methods=['POST'])
def gconnect():
    CLIENT_ID = json.loads(
        open('client_secrets.json', 'r').read())['web']['client_id']
    # Validate state token
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    # Obtain authorization code
    code = request.data

    try:
        # Upgrade the authorization code into a credentials object
        oauth_flow = flow_from_clientsecrets('client_secrets.json', scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(json.dumps('Failed to upgrade the authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Check that the access token is valid.
    access_token = credentials.access_token
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s' % access_token)
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])
    # If there was an error in the access token info, abort.
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is used for the intended user.
    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(
            json.dumps("Token's user ID doesn't match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is valid for this app.
    if result['issued_to'] != CLIENT_ID:
        response = make_response(
            json.dumps("Token's client ID does not match app's."), 401)
        print "Token's client ID does not match app's."
        response.headers['Content-Type'] = 'application/json'
        return response

    stored_access_token = login_session.get('access_token')
    stored_gplus_id = login_session.get('gplus_id')
    if stored_access_token is not None and gplus_id == stored_gplus_id:
        response = make_response(json.dumps('Current user is already connected.'),200)
        response.headers[' -Type'] = 'application/json'
        return response

    # Store the access token in the session for later use.
    login_session['access_token'] = credentials.access_token
    login_session['gplus_id'] = gplus_id

    # Get user info
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': credentials.access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)

    data = answer.json()

    login_session['username'] = data["name"]
    login_session['picture'] = data["picture"]
    login_session['email'] = data["email"]



    output = ''
    output += '<h1>Welcome, '
    output += login_session['username']
    output += '!</h1>'
    output += '<img src="'
    output += login_session['picture']
    output += ' " style = "width: 300px; height: 300px;border-radius: 150px;-webkit-border-radius: 150px;-moz-border-radius: 150px;"> '
    flash("you are now logged in as %s" %login_session['username'])
    print "done!"
    return output

# User Helper Functions


def createUser(login_session):
    newUser = User(name=login_session['username'], email=login_session[
                   'email'], picture=login_session['picture'])
    session.add(newUser)
    session.commit()
    user = session.query(User).filter_by(email=login_session['email']).one()
    return user.id


def getUserInfo(user_id):
    user = session.query(User).filter_by(id=user_id).one()
    return user


def getUserID(email):
    try:
        user = session.query(User).filter_by(email=email).one()
        return user.id
    except:
        return None

# DISCONNECT - Revoke a current user's token and reset their login_session


@app.route('/gdisconnect')
def gdisconnect():
    # Only disconnect a connected user.
    access_token = login_session.get('access_token')
    if access_token is None:
        response = make_response(
            json.dumps('Current user not connected.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' % access_token
    h = httplib2.Http()
    result = h.request(url, 'GET')[0]
    if result['status'] == '200':
        response = make_response(json.dumps('Successfully disconnected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        return response
    else:
        response = make_response(json.dumps('Failed to revoke token for given user.', 400))
        response.headers['Content-Type'] = 'application/json'
        return response




@app.route('/')
@app.route('/home')
def homepage():
    return render_template('homepage.html')


@app.route('/student/<int:ID>/')
def showStudent(ID, sesh):
    student = sesh.query(Student).filter_by(id=ID).one()
    student_info = { "first_name" : student.first_name
                , "last_name" : student.last_name
                }
    return student_info

@app.route('/trips')
def showTrips():
    return render_template('trips.html')

def newTrip():
    pass
    #SAME AS NEWUNIVERSE IN ITEM CATALOG?
    """TODO: IMPLEMENT"""

@app.route('/student/<int:ID>')
def showStudentPref(ID, sesh):
    preferences = sesh.query(Preference).filter_by(student_id=ID).all()
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
        return "it worked"
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

@app.route('/disconnect')
def disconnect():
    if 'provider' in login_session:
        if login_session['provider'] == 'google':
            gdisconnect()
            del login_session['gplus_id']
            del login_session['access_token']

        del login_session['username']
        del login_session['email']
        del login_session['picture']
        del login_session['user_id']
        del login_session['provider']
        flash("You have successfully been logged out.")
        return redirect(url_for('showStudents'))
    else:
        flash("You were not logged in")
        return redirect(url_for('showStudents'))



if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
