import flask
from flask import Flask, request
from sqlalchemy import create_engine, asc, desc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Student, PreferredMember

engine = create_engine('sqlite:///database.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

def getStudents():
    session = DBSession()
    students = session.query(Student).all()
    return students
