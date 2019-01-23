# prototype of group sorting algorithm
import sys
import flask
from flask import Flask, render_template, request
from sqlalchemy import create_engine, asc, desc
from sqlalchemy.orm import sessionmaker
from database_setup_no_gender import Base, Student, engine, Preference
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

app = Flask(__name__)
engine = create_engine('sqlite:///database.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# ***********************
# Constants
# ***********************

max_prefs = 4
num_of_groups = 4
# this should be calculated or set by user


# ***********************
# Functions
# ***********************

# ------------------------
# Output student list
# ------------------------


def print_student_list():
    print("Student list size:" + str(len(students)))
    for student in students:
        student.prefList()


# ------------------------
# Output All Groups
# ------------------------


def print_all_groups():
    print("Number of Groups:" + str(len(Groups)))

    for count in range(len(Groups)):
        print("")
        print("Group " + str(count + 1))
        for student in Groups[count]:
            print(student.name)


def get_all_groups():
    groups = []
    for count in range(len(Groups)):
        group = []
        group.append("Group " + str(count + 1))
        for student in Groups[count]:
            group.append(student.name)
        groups.append(group)
    return groups


# --------------------------------------------
# Find lowest matching pref_score in a group
# --------------------------------------------


def pref_in_group(student, group):
    lowest_pref_score_match = Student_class("None", 0, -1, False, "")
    first_match = True
    for preference in student.prefs:
        if preference in group:
            if first_match is True:
                lowest_pref_score_match = preference
                first_match = False
            elif preference.pref_score < lowest_pref_score_match.pref_score:
                lowest_pref_score_match = preference
    return lowest_pref_score_match


# return the Student object with the lowest pref_score

# ------------------------------------------------------------------------
# checks to see if a student is already in a group with a preference
# ------------------------------------------------------------------------


def is_in_same_group(student, pref):
    alreadyAssigned = False
# initialize return assuming there is no existing preference in a group

    for searchGroup in Groups:
        pair = [student, pref]
# print "checking same group " + student.name + " with " + pref.name
        if all(x in searchGroup for x in pair):
            # x is just the comparison variable used
            # will return True is student and pref are in searchGroup together
            # print "match"
            alreadyAssigned = True
    return alreadyAssigned


# --------------------------------------------
# Output Statitics
# --------------------------------------------


def print_stats(students):

    # initialize prefs_count
    prefs_count = []
    for i in range(max_prefs + 1):
        prefs_count.append(0)

    for student in students:
        prefs_matched = 0
        print ""
        for preference in student.prefs:
            if is_in_same_group(student, preference) is True:
                prefs_matched += 1

        print student.name + " preferences matched is " + str(prefs_matched)
        prefs_count[prefs_matched] += 1

    print ""
    for preference in prefs_count:
        print str(prefs_count.index(preference)) + " matches = " + str(preference)

    print""
    group_length = 0
    empty_group = 0
    for g in Groups:
        if g == []:
            empty_group += 1
        else:
            group_length += len(g)
    print "The average group size is " + \
    str(group_length/(len(Groups) - empty_group))
    print "There are " + str(empty_group) + " empty groups"

#***********************
# Main Program
# ***********************

# ------------------
# Initialize Data
# ------------------


def get_students():
    students = []
    student_query = session.query(Student).all()
    preference_query = None
    count = 1
    # makes a list of Student objects from the database
    for student in student_query:
        preference_query = session.query(Preference).filter_by(student_id=count).all()
        students.append(Student_class(student.first_name, -1, -1, False, preference_query))
        count = count + 1
    return students


def sort_students(students):
    students.sort(key=lambda students: (students.pref_score, students.mutual_score), reverse=True)
    return students


def score_students(students):
    for primary_student in students:
        for comparison_student in students:
            for index in range(max_prefs):
                if(comparison_student.name == primary_student.prefs[index].name):
                    comparison_student.pref_score += 1
                    for secondary_index in range(len(primary_student.prefs)):
                        if(comparison_student.prefs[secondary_index].name == primary_student.name):
                            comparison_student.mutual_score += 1
    return None


def convert_pref_student(students):
    pref = []
    for primary_student in students:
        for comparison_student in students:
            for index in range(4):
                if(comparison_student.name == primary_student.prefs[index].name):
                    pref.append(comparison_student)
        primary_student.prefs = pref
        pref = []


def concatenate_names(students):
    for student in students:
        for index in range(len(student.prefs)):
            student.prefs[index].name = student.prefs[index].first_name1 + student.prefs[index].last_name1
    return None


# Create Groups

Groups = []


def setup():
    for iterate in range(num_of_groups):  # initialize groups
        Groups.append([])


# -------------------------------
# Assign students to Groups
# -------------------------------
def order_groups(students, student):
    group_order = []

# get info for each group
    for count in range(num_of_groups):
        group_order.append(["", "", ""])
        group_order[count][0] = count
        group_order[count][1] = len(Groups[count])
        lowest_pref = pref_in_group(student, Groups[count])
        group_order[count][2] = lowest_pref.pref_score

# sort group_order by groupSize then by lowest preference score of a preference
    group_order.sort(
        key=lambda l: (l[1], l[2])
    )
    return group_order

def condition_g(try_to_pull_preference_with_student, student, group_order, group_index):
    if student.is_assigned is False and \
            try_to_pull_preference_with_student is False:
        # if not, then need to find another group with a preference
        if pref_in_group(s, Groups[group_order[group_index][0]]).name != "None":
            students.is_assigned = True
# mark student as assigned to move to the next student
            Groups[group_order[group_index][0]].append(s)

def condition_f(try_to_pull_preference_with_student, student, group_order, group_index):
    if student.is_assigned is False and \
            try_to_pull_preference_with_student is True:

        # sort preferences by pref-score from highest to lowest
        student.prefs.sort(key=lambda l: l.pref_score, reverse=True)
        pulled_preference_with_student = False
        for preference in student.prefs:
            # for each preference for a student
            # if unassigned and prefs-unassigned > 1
            # pull into group.  Condition (F)
            if preference.is_assigned is False and \
                preference.prefsUnAssigned(num_of_groups, Groups) > 1 and \
                    student.is_assigned is False:
                student.is_assigned = True
# mark student as assigned to move to the next student
                preference.is_assigned = True
# mark the preference as assigned too
                Groups[group_order[group_index][0]].append(student)
# add Student to the group
                Groups[group_order[group_index][0]].append(preference)
# add the students preference to the group (pull)
                pulled_preference_with_student = True
# found a preference to pull into group with student
        try_to_pull_preference_with_student = False
# don't try to pull a preference when processing the remaining groups
        condition_d(pulled_preference_with_student, student, group_order, group_index)

def condition_d(pulled_preference_with_student, student, group_order, group_index):
    if pulled_preference_with_student is False:
        # if couldn't pull in a preference with the student
        # check to see if there is a preference in the group
        if pref_in_group(student, Groups[group_order[group_index][0]]).name \
                != "None":
            student.is_assigned = True
            Groups[group_order[group_index][0]].append(student)

def condition_a_b(student):
    already_assigned_with_a_preference = False
    for preference in student.prefs:
        if is_in_same_group(student, preference) is True:
            already_assigned_with_a_preference = True
# pull highest pref-score preference into the same group
    if already_assigned_with_a_preference is False:
        student.prefs.sort(key=lambda l: l.pref_score, reverse=True)
# sort prefs by highest pref-score
        for preference in student.prefs:
            if preference.is_assigned is False:
                # check to see if pref is not already assigned
                g_index = student.inGroup(Groups)
                Groups[g_index].append(preference)
# add the students preference to the group (pull).  Condition (B)
                preference.is_assigned = True
# mark is assigned
                break

def assign_students(students):
    for student in students:
        # process entire student list
        # if student is NOT assigned
        if student.is_assigned is False:
            group_order = order_groups(students, student)
# -----------------------------------
# Process each group for a student
# -----------------------------------
            try_to_pull_preference_with_student = True
# first try to pull a preference with the student into the smallest group
            for group_index in range(num_of_groups):
                # Condition (G) and (H)
                # check to see if there were no options to pull a preference
                condition_g(try_to_pull_preference_with_student, student, group_order, group_index)
# add Student to the group
                if student.is_assigned is True:
                        break
# don't process anymore groups
# Condition (F)
                condition_f(try_to_pull_preference_with_student, student, group_order, group_index)

                if student.is_assigned is True:
                            break
        else:
            condition_a_b(student)

def unassigned_students(stu):
    students = []
    for student in stu:
        if student.is_assigned == False:
            students.append(student)
    print str(len(students)) + " students are unable to be assigned"
    if len(students) != 0:
        print "The following students are unassigned:"
    for student in students:
        print student.name


asdf=get_students()
concatenate_names(asdf)
#sort_students(asdf)
score_students(asdf)
sort_students(asdf)
convert_pref_student(asdf)
setup()
assign_students(asdf)
print_all_groups()
unassigned_students(asdf)
print_stats(asdf)
