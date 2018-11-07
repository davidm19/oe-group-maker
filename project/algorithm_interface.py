import flask
from flask import Flask, render_template, request, redirect, jsonify, url_for, flash
from sqlalchemy import create_engine, asc, desc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Student, engine, Preference
from flask import session as login_session
import random, string
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests

DBSession = sessionmaker(bind=engine)
session = DBSession()

'''

ALGORITHM INTERFACE
1. select trip from database
2. algorithm step 1
3. algorithm step 2
4. algorithm step 3
5. export list in some format

'''

'''
selects students from grade level
'''
def getstudents_by_gradelevel():
    #trip = session.query(Trip).filter_by(id=)
    pass

'''
selects students from trip ID
'''
def getstudents_by_tripID():
    pass

'''
part 1 of algorithm
'''
def alg_part1():
    pass

'''
part 2 of algorithm
'''
def alg_part2():
    pass

'''
part 3 of algorithm
'''
def alg_part3():
    pass

'''
exports the final list
'''
def export_list():
    pass