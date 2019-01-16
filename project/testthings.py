# project/test_basic.py
from flask import Flask, render_template, request, redirect, url_for, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from testalg_database_setup import Base, Student, engine, Preference
import os
import unittest
from application import showStudent, showStudents, showStudentPref, newStudent
from application import session, app
from improved_algorithm_interface import get_students, concatenate_names
from improved_algorithm_interface import score_students, sort_students
from improved_algorithm_interface import convert_pref_student, setup
from improved_algorithm_interface import assign_students, print_all_groups
from improved_algorithm_interface import get_all_groups
from Student_class import Student_class


app = Flask(__name__)
engine = create_engine('sqlite:///database.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


class BasicTests(unittest.TestCase):

    def test_alg(self):
        students = get_students()
        concatenate_names(students)
        score_students(students)
        sort_students(students)
        convert_pref_student(students)
        setup()
        assign_students(students)
        print(get_all_groups())
        results = get_all_groups()
        expected_results = [['Group 1', 'Jack', 'Fred', 'Kobe',
                            'James', 'Durant'],
                            ['Group 2', 'Tej', 'Bob', 'Magic',
                            'Patrick', 'Horry'],
                            ['Group 3', 'Frank', 'Manny',
                                'Kareem', 'Lebron', 'Byron'],
                            ['Group 4', 'Jonathan', 'Shaq',
                                'Curry', 'Worthy', 'Joe'],
                            ['Group 5', 'Jordan', 'Jerry',
                                'Reggie', 'Nev', 'Gasol'],
                            ['Group 6', 'Cooper', 'Rambus',
                            'Fisher', 'Wilt', 'Moe']]
        self.assertEqual(results, expected_results)


if __name__ == "__main__":
    unittest.main()
