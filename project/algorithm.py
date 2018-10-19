import flask
from flask import Flask, request
from server.dao import Customer, engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Student, PreferredMember

def getStudents():
    students = query.all()
    return students
