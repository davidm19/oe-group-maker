# prototype of group sorting algorithm
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

app = Flask(__name__)
engine = create_engine('sqlite:///database.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# ***********************
# Constants
# ***********************

max_prefs = 4
num_of_groups = 6
# this should be calculated or set by user


# ***********************
# Functions
# ***********************

# ------------------------
# Output student list
# ------------------------


def print_student_list():
    print("Student list size:" + str(len(students)))
    for x in students:
        x.prefList()


# ------------------------
# Output All Groups
# ------------------------


def print_all_groups():
    print("Number of Groups:" + str(len(Groups)))

    for x in range(len(Groups)):
        print("")
        print("Group " + str(x + 1))
        for y in Groups[x]:
            print(y.name)


def get_all_groups():
    groups = []
    for x in range(len(Groups)):
        group = []
        group.append("Group " + str(x + 1))
        for y in Groups[x]:
            group.append(y.name)
        groups.append(group)
    return groups


# --------------------------------------------
# Find lowest matching pref_score in a group
# --------------------------------------------


def pref_in_group(student, group):
    lowest_pref_score_match = Student_class("None", 0, 99999, False, "")
    first_match = True
    for p in student.prefs:
        if p in group:
            if first_match is True:
                lowest_pref_score_match = p
                first_match = False
            elif p.pref_score < lowest_pref_score_match.pref_score:
                lowest_pref_score_match = p
    return lowest_pref_score_match


# return the Student object with the lowest pref_score

# ------------------------------------------------------------------------
# checks to see if a student is already in a group with a preference
# ------------------------------------------------------------------------


def is_in_same_group(student, pref):
    already_assigned = False
# initialize return assuming there is no existing preference in a group

    for search_group in Groups:
        pair = [student, pref]
# print "checking same group " + student.name + " with " + pref.name
        if all(x in search_group for x in pair):
            # will return True is student and pref are in search_group together
            # print "match"
            already_assigned = True
    return already_assigned


# --------------------------------------------
# Output Statitics
# --------------------------------------------


def printStats(students):

    # initialize prefs_count
    prefs_count = []
    for i in range(max_prefs + 1):
        prefs_count.append(0)

    for s in students:
        prefs_matched = 0
        print ""
        for p in s.prefs:
            if is_in_same_group(s, p) is True:
                prefs_matched += 1

        print s.name + " preferences matched is " + str(prefs_matched)
        prefs_count[prefs_matched] += 1

    print ""
    for p in prefs_count:
        print str(prefs_count.index(p)) + " matches = " + str(p)

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
    temp1 = session.query(Student).all()
    temp2 = None
    temp3 = []
    count = 1
    # makes a list of Student objects from the database
    for i in temp1:
        temp2 = session.query(Preference).filter_by(student_id=count).all()
        students.append(Student_class(i.first_name, -1, -1, False, temp2))
        count = count + 1
    return students


def sort_students(l):
    l.sort(key=lambda l: (l.pref_score, l.mutualScore), reverse=True)
    return l


def score_students(students):
    for i in students:
        for x in students:
            for y in range(max_prefs):
                if(x.name == i.prefs[y].name):
                    x.pref_score += 1
                    for a in range(len(i.prefs)):
                        if(x.prefs[a].name == i.name):
                            x.mutualScore += 1
    return None


def convert_pref_student(students):
    pref = []
    for i in students:
        for x in students:
            for y in range(4):
                if(x.name == i.prefs[y].name):
                    pref.append(x)
        i.prefs = pref
        pref = []


def concatenate_names(students):
    for i in students:
        for y in range(len(i.prefs)):
            i.prefs[y].name = i.prefs[y].first_name1 + i.prefs[y].last_name1
    return None


# Create Groups

Groups = []


def setup():
    for x in range(num_of_groups):  # initialize groups
        Groups.append([])


# -------------------------------
# Assign students to Groups
# -------------------------------


def assign_students(students):
    for s in students:
        # process entire student list

        # if student is NOT assigned
        if s.is_assigned is False:

            # -----------------------------------
            # Determine order to process Groups
            # -----------------------------------
            # determine the Group order to process.
            # Find smallest sized groups
            # if equal then sort by the lowest pref_score
            # group_order is a list of (group index, group size, lowest)

            group_order = []

# get info for each group
            for x in range(num_of_groups):
                group_order.append(["", "", ""])
                group_order[x][0] = x
                group_order[x][1] = len(Groups[x])
                lowest_pref = pref_in_group(s, Groups[x])
                group_order[x][2] = lowest_pref.pref_score

# sort group_order by groupSize then by lowest preference score of a preference
            group_order.sort(
                key=lambda l: (l[1], l[2])
            )
# print group_order

# -----------------------------------
# Process each group for a student
# -----------------------------------
            try_to_pull_preference_with_student = True
# first try to pull a preference with the student into the smallest group
            for i in range(num_of_groups):

                # Condition (G) and (H)
                # check to see if there were no options to pull a preference
                if s.is_assigned is False and \
                        try_to_pull_preference_with_student is False:
                    # if not, then need to find another group with a preference
                    if pref_in_group(s, Groups[group_order[i][0]]).name != "None":
                        s.is_assigned = True
# mark student as assigned to move to the next student
                        Groups[group_order[i][0]].append(s)
# add Student to the group
                        break
# don't process anymore groups
# Condition (F)
                # check if not assigned to skip processing other groups
                if s.is_assigned is False and \
                        try_to_pull_preference_with_student is True:

                    # sort preferences by pref-score from highest to lowest
                    s.prefs.sort(key=lambda l: l.pref_score, reverse=True)
# check for Condition (F)
                    pulled_pref_with_student = False
                    for p in s.prefs:
                        # for each preference for a student
                        # if unassigned and prefs-unassigned > 1
                        # pull into group.  Condition (F)
                        if p.is_assigned is False and \
                            p.prefs_unassigned(num_of_groups, Groups) > 1 and \
                                s.is_assigned is False:
                            s.is_assigned = True
# mark student as assigned to move to the next student
                            p.is_assigned = True
# mark the preference as assigned too
                            Groups[group_order[i][0]].append(s)
# add Student to the group
                            Groups[group_order[i][0]].append(p)
# add the students preference to the group (pull)
                            pulled_pref_with_student = True
# found a preference to pull into group with student
                    try_to_pull_preference_with_student = False
# don't try to pull a preference when processing the remaining groups

                    if pulled_pref_with_student is False:
                        # if couldn't pull in a preference with the student
                        # check to see if there is a preference in the group
                        if pref_in_group(s, Groups[group_order[i][0]]).name \
                                != "None":
                            s.is_assigned = True
# mark student as assigned to move to the next student
                            Groups[group_order[i][0]].append(s)
# add Student to the group
                            break
        else:
            # if student IS assigned
            already_assigned_with_a_pref = False
# need to check multiple cases
# this variable will move to next student after an assignment condition is met
# check to see if already assigned with a preference.  Condition (A)
            for p in s.prefs:
                if is_in_same_group(s, p) is True:
                    already_assigned_with_a_pref = True
# pull highest pref-score preference into the same group
            if already_assigned_with_a_pref is False:
                s.prefs.sort(key=lambda l: l.pref_score, reverse=True)
# sort prefs by highest pref-score
                for p in s.prefs:
                    if p.is_assigned is False:
                        # check to see if pref is not already assigned
                        g_index = s.in_group(Groups)
                        Groups[g_index].append(p)
# add the students preference to the group (pull).  Condition (B)
                        p.is_assigned = True
# mark is assigned
                        break
# don't check anymore preferences if found one to pull into group

def unassigned_students(stu):
    students = []
    for s in stu:
        if s.is_assigned == False:
            students.append(s)
    print str(len(students)) + " students are unable to be assigned"
    if len(students) != 0:
        print "The following students are unassigned:"
    for i in students:
        print i.name
