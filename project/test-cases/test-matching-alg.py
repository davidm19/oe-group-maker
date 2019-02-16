import flask
from flask import Flask, request
from sqlalchemy import create_engine, asc, desc
from sqlalchemy.orm import sessionmaker
from collections import defaultdict
from database_setup import Base, Student, PreferredMember

engine = create_engine('sqlite:///database.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
