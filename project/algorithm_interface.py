import flask
from flask import Flask, render_template, request, redirect, jsonify, url_for
from flask import flash
from sqlalchemy import create_engine, asc, desc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Student, engine, Preference
from flask import session as login_session
import random
import string
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests

DBSession = sessionmaker(bind=engine)
session = DBSession()


def getstudents_by_gradelevel(gradeLevel):
    return session.query(Student).filter_by(grade=gradeLevel).all()


def getstudents_by_tripID(tripID):
    return session.query(Trip).filter_by(id=tripID).all()


def temp_partner(studentID):
    return session.query(Preference).filter_by(student_id=studentID).one()


def removal1(student):
    student.Partner = session.query(Preference).filter_by(studentID)


def lowpref_removal(stuID):
    pass


def removal2():
    pass


def alg_part1():
    pass


def alg_part2():
    pass


def alg_part3():
    pass


def export_list():
    pass
