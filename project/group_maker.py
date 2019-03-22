#from improved_algorithm_interface.py import *
import improved_algorithm_interface
import sys
import flask
from flask import Flask, render_template, request
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
from Student_class import Student_class

asdf=improved_algorithm_interface.get_students()
improved_algorithm_interface.concatenate_names(asdf)
improved_algorithm_interface.score_students(asdf)
improved_algorithm_interface.sort_students(asdf)
improved_algorithm_interface.convert_pref_student(asdf)
improved_algorithm_interface.setup()
improved_algorithm_interface.assign_students(asdf)
improved_algorithm_interface.printAllGroups()
improved_algorithm_interface.unassigned_students(asdf)
improved_algorithm_interface.printStats(asdf)
