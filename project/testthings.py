# project/test_basic.py
from flask import Flask, render_template, request, redirect, url_for, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from testalg_database_setup import Base, Student, engine, Preference
import os
import unittest
from application import showStudent, showStudents, showStudentPref, newStudent
from application import session, app
from algorithm_interface import remove_lowpriority_pairs, check_for_mutual_pref
from Student import Student_class


app = Flask(__name__)
engine = create_engine('sqlite:///testalg_database.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


class BasicTests(unittest.TestCase):

    # def test_showStudent(self):
    #     expected_results = { "first_name" : "Michael"
    #                 , "last_name" : "Huang"
    #                 }
    #     results = showStudent(1, session)
    #     self.assertEqual(results, expected_results)
    #
    # def test_temp_partner(self):
    #     expected_results = {
    #     }
    #     results = temp_partner()
    #     self.assertEqual()
    #
    # def test_remove_one_student(self):
    #     expected_results = {}
    #     results = remove_one_student()
    #     self.assertEqual()
    #


    def test_stepTwo(self):
        newStudent('Char', 'Lie', 'Paul', 'Sam', 'Kel', session)
        newStudent('Pete', 'R', 'Kel', 'Sam', 'Paul', session)
        newStudent('Eli', 'S', 'Sam', 'Kel', 'Char', session)
        newStudent('Paul', 'Ly', 'Eli', 'Char', 'Sam', session)
        newStudent('Kel', 'Ly', 'Pete', 'Char', 'Sam', session)
        newStudent('Sam', 'My', 'Char', 'Paul', 'Kel', session)
        students = session.query(Student).all()
        for student in students:
            remove_lowpriority_pairs(student, session)
        students_info = []
        for student in students:
            check_for_mutual_pref(student,session)
        students = session.query(Student).all()
        preferences = session.query(Preference)
        for student in students:
            new_preferences = preferences.filter_by(student_id = student.id).all()
            student_info = [student.first_name, student.last_name]
            students_info.append(student_info)
            # print(student.first_name)
            # print(student.last_name)
            for p in new_preferences:
                students_info.append(p.name)
                # print(p.name)

        expected_results = [['Char', 'Lie'], 'Paul', 'Sam', ['Pete', 'R'], 'Kel', ['Eli','S'], 'Sam', 'Kel', ['Paul','Ly'], 'Eli', 'Char', ['Kel', 'Ly'], 'Pete', ['Sam', 'My'], 'Char']
        results = students_info
        self.maxDiff = None
        print("results")
        print(results)
        print("\n")
        print("expected results")
        print(expected_results)
        self.assertEqual(results, expected_results)
        if results == expected_results:
            print(",@@@@@@@@@@,,@@@@@@@%  .#&@@@&&.,@@@@@@@@@@,      %@@@@@@%*   ,@@@%     .#&@@@&&.  *&@@@@&(  ,@@@@@@@%  %@@@@@,     ,@@,")
            print("            ,@@,    ,@@,      ,@@/   ./.    ,@@,          %@%   ,&@# .&@&@@(   .@@/   ./. #@&.  .,/  ,@@,       %@%  *&@&.  ,@@,")
            print("            ,@@,    ,@@&%%%%. .&@@/,        ,@@,          %@%   ,&@# %@& /@@,  .&@@/,     (@@&%(*.   ,@@&%%%%.  %@%    &@#  ,@@,")
            print("            ,@@,    ,@@/,,,,    ./#&@@@(    ,@@,          %@@@@@@%* /@@,  #@&.   ./#&@@@(   *(%&@@&. ,@@/,,,,   %@%    &@#  .&&.")
            print("            ,@@,    ,@@,      ./,   .&@#    ,@@,          %@%      ,@@@@@@@@@% ./.   .&@# /*.   /@@. ,@@,       %@%  *&@&.   ,,")
            print("            ,@@,    ,@@@@@@@% .#&@@@@&/     ,@@,          %@%     .&@#     ,@@/.#&@@@@&/   /%&@@@@.  ,@@@@@@@%  %@@@@@.     ,@@,")
            print(",*************,,*/(((((//,,*(#%%%%%%%%%%%%%%%#(*,,,****************************************************,*/(((((((((/((((////****/((##%%%%%%")
            print(",*************,,//((((((//,,*(%%%%%%%%%%%%%%%%%##/*****************************************************,,*/(///(//////****//((##%%%%%%%%%%%")
            print(",************,,*/(((((((//***/#%%%%%%%%%%%%%%%%%%%#(/***************************************************,*//////////*//((#%%%%%%%%%%%%%%%%%")
            print(",***********,,*////////////***/##%%%%%%%%%%%%%%%%%%%##(*,***********************************************,,*////////(###%%%%%%%%%%%%%%%%%%%%")
            print(",**********,,,*/*******//////**/(#%%%%%%%%%%%%%%%%%%%%%#(/**********************************************,,,***/(##%%%%%%%%%%%%%%%%%%%%%%%%%")
            print(",*********,,,,*************///***/(#%%%%%%%%%%%%%%%%%%%%%%#(/***********************************,****,****/((#%%%%%%%%%%%%%%%%%%%%%%%%%%%%#")
            print(",*********,,,***************//****/(##%%%%%%%%%%%%%%%%%%%%%%##//**************//////////////////////((#####%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#(")
            print(",********,,,,***********************/(#%%%%%%%%%%%%%%%%%%%%%%%##################%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%##(/")
            print(",*******,..,***********************,,*/##%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%###((//")
            print(",*******,.,,***********************,,,,*(#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%##(//**//")
            print(",******,.,,,************************,,,,*/(#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#(//*******")
            print(",*****,,,,,********,***,,,,,,,,,,,,*,,,,,,*/(######%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%##(/**********")
            print(",*****,..,*******,,,,,,,,,,,,,,,,,,,,,,*,,,,*///((#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%###(/************")
            print(",*****,,,*******,,,,,*,,,,,,,,,,,,,,,,,****,,,*/(#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#######(//**************")
            print(",****,.,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,**,,,/(%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#((//******************")
            print(",***,..,,,,,,,,,,,,,,,,,,,,,,,,,,,,,..,,,,,,,*(#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#(/*******************")
            print(",**,,.,,,,,,,,,,,,,,,,,,,,,,,,,,.......,,,,,,/#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#####%%%%%%%%%%%%%%%%#(/******************")
            print(",**,..,,,,,,,,,,,,,,,,,,,,,,,,,......,,,*,,,*(#%%%%%%%%##(((/(##%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%##(((/*/((#%%%%%%%%%%%%%%#(/*****************")
            print(",*,..,,,,,,,,,,,,,,,,,,,,,,,,,,,.....,,**,,*/#%%%%%%%##((((*,**/#%%%%%%%%%%%%%%%%%%%%%%%%%%%%##((##/,,,*(#%%%%%%%%%%%%%%#(*****************")
            print(".*,.,,,**,,,,,,,,,,,,,,,,,,,,,,,,,,*****,,,/(%%%%%%%%#(//(#/,..*/#%%%%%%%%%%%%%%%%%%%%%%%%%%%#(//(#/,..,/(#%%%%%%%%%%%%%%#/*****///////////")
            print(".,..,,,,,,,,,,,,,,,,,,,,,,,,,,*,,*******,,,(#%%%%%%%%#(*,,,....,/#%%%%%%%%%%%%%%%%%%%%%%%%%%%#(*,,,....,/(#%%%%%%%%%%%%%%#(*,**////////////")
            print(".,..,,,,,,,,,...........,,,,,,*,********,,*(#%%%%%%%%%#(/*,,...,/#%%%%%%%%%%%%%%%%%%%%%%%%%%%%#(/*,,..,*/##%%%%%%%%%%%%%%%#(***////////////")
            print("...,,,,,,,................,,*,**********,,/#%%%%%%%%%%%%#((////((#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%##((///(#%%%%%%%%%%%%%%%%%%(/**////////////")
            print(" ..,,,,,,.................,,,**********,,*(#%%%%%%%%%%%%%%%%%%#%%%%%%%%#((///((#%%%%%%%%%%%%%%%%%%%%%#%%%%%%%%%%%%%%%%%%%%%#/**////////////")
            print(".,,,,,,,,.................,,***********,,/(####%%%%%%%%%%%%%%%%%%%%%%%%#(/*,,,*(#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#(/*////////////")
            print(".,***,,,,,,..............,,,**********,..,***//((##%%%%%%%%%%%%%%%%%%%%%%%##((##%%%%%%%%%%%%%%%%%%%%%%%%%##(((((((((###%%%%%#/**///////////")
            print(".*****,,,,,,,,,,,,,,,,,,,*************,..,*******/(#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%##///*//////((#%%%%%#(**///////////")
            print(".****************/******/***////*****,.,*///////**/#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#(////////////(#%%%%%#/**//////////")
            print(".***********************/////*******,..,*//////////(#%%%%%%%%%%%%%%%%%%%%##########%%%%%%%%%%%%%%%%%%%%#(///////////*/(#%%%%%#(***/////////")
            print(".************************///********,..,*//////////#%%%%%%%%%%%%%%%%%%#(//*****///(((##%%%%%%%%%%%%%%%%#(///////////**/##%%%%##/***////////")
            print(".***********************************,.,,***///////(#%%%%%%%%%%%%%%%%#(/*,,,*//((((////(#%%%%%%%%%%%%%%%#((////////////(#%%%%%%#(*********//")
            print(",***********,,,*,,*,,**************,,,*//******//(#%%%%%%%%%%%%%%%%%#(*,,*/(((#####(((((#%%%%%%%%%%%%%%%##///////////(#%%%%%%%%#(***///////")
            print(",*************,,**,,,************,,,,,/(##((((####%%%%%%%%%%%%%%%%%%%(/**/(((#((((#((//(#%%%%%%%%%%%%%%%%%#(((((((((##%%%%%%%%%%#/**///////")
            print(",******************************,,,,,,,*(#%#%%%%%%%%%%%%%%%%%%%%%%%%%%#(**/((#(#(((#((//(#%%%%%%%%%%%%%%%%%%%%%%%#%#%%%%%%%%%%%%%#(**///////")
            print(",*************,**************,****,,,,,/(#%%%%%%%%%%%%%%%%%%%%%%%%%%%%#(/*/((((#((((///(#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%(/*///////")
            print(",*************************************,*/#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%##(////////////(#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#/**/////*")
            print(",******////****///////////////////////***/#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%####(((((((###%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#(********")
            print(".,*,****///////////////////////////////***/#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#(/*******")
            print(".,,,,*****//////////////////////////*******(#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%##(*******")
            print(".,,,,,,***********/////////////////********/(#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%(*******")


    # def test_stepTwoPrelim(self):
    #     newStudent('Char', 'Lie', 'Paul', 'Sam', 'Kel', session)
    #     newStudent('Pete', 'R', 'Kel', 'Sam', 'Paul', session)
    #     newStudent('Eli', 'S', 'Sam', 'Kel', 'Char', session)
    #     newStudent('Paul', 'Ly', 'Eli', 'Char', 'Sam', session)
    #     newStudent('Kel', 'Ly', 'Pete', 'Char', 'Sam', session)
    #     newStudent('Sam', 'My', 'Char', 'Paul', 'Kel', session)
    #     students = session.query(Student)
    #     char = students.filter_by(first_name = 'Char').one()
    #     remove_lowpriority_pairs(char, session)
    #     students_info = []
    #     students = session.query(Student).all()
    #     preferences = session.query(Preference)
    #     for student in students:
    #         new_preferences = preferences.filter_by(student_id = student.id).all()
    #         student_info = [student.first_name, student.last_name]
    #         students_info.append(student_info)
    #         # print(student.first_name)
    #         # print(student.last_name)
    #         for p in new_preferences:
    #             students_info.append(p.name)
    #             # print(p.name)
    #
    #     expected_results = [['Char', 'Lie'], 'Paul', 'Sam', 'Kel', ['Pete', 'R'], 'Kel', 'Sam', 'Paul', ['Eli','S'], 'Sam', 'Kel', 'Char', ['Paul','Ly'], 'Eli', 'Char', ['Kel', 'Ly'], 'Pete', 'Char', 'Sam', ['Sam', 'My'], 'Char', 'Kel']
    #     results = students_info
    #     self.maxDiff = None
    #     self.assertEqual(results, expected_results)
    #     # self.assertEqual("yes","yes")

    # def test_test(self):
    #     newStudent('Char', 'Lie', 'Paul', 'Sam', 'Kel', session)
    #     newStudent('Pete', 'R', 'Kel', 'Sam', 'Paul', session)
    #     newStudent('Eli', 'S', 'Sam', 'Kel', 'Paul', session)
    #     newStudent('Paul', 'Ly', 'Eli', 'Char', 'Sam', session)
    #     newStudent('Kel', 'Ly', 'Pete', 'Char', 'Sam', session)
    #     newStudent('Sam', 'My', 'Char', 'Paul', 'Eli', session)
    #     students_info = []
    #     students = session.query(Student).all()
    #     preferences = session.query(Preference)
    #     for student in students:
    #         new_preferences = preferences.filter_by(student_id = student.id).all()
    #         student_info = [student.first_name, student.last_name]
    #         students_info.append(student_info)
    #         for p in new_preferences:
    #             students_info.append(p.name)
    #             print(p.name)
    #     expected_results = [['Char', 'Lie', 'Paul', 'Sam', 'kel'],['Pete', 'R', 'Kel', 'Sam', 'Paul'], ['Eli','S', 'Sam', 'Kel', 'Paul'], ['Paul', 'Ly', 'Eli', 'Char', 'Sam'], ['Kel', 'Ly', 'Pete', 'Char', 'Sam'], ['Sam', 'My', 'Char', 'Paul', 'Eli']]
    #     results = students_info
    #     self.assertEqual(results, expected_results)

if __name__ == "__main__":
    unittest.main()
