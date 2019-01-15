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

maxPrefs = 4
numOfGroups = 6
# this should be calculated or set by user


# ***********************
# Functions
# ***********************

# ------------------------
# Output student list
# ------------------------


def printStudentList():
    print("Student list size:" + str(len(students)))
    for x in students:
        x.prefList()


# ------------------------
# Output All Groups
# ------------------------


def printAllGroups():
    print("Number of Groups:" + str(len(Groups)))

    for x in range(len(Groups)):
        print("")
        print("Group " + str(x + 1))
        for y in Groups[x]:
            print(y.name)


def getAllGroups():
    groups = []
    for x in range(len(Groups)):
        group = []
        group.append("Group " + str(x + 1))
        for y in Groups[x]:
            group.append(y.name)
        groups.append(group)
    return groups


# --------------------------------------------
# Find lowest matching prefScore in a group
# --------------------------------------------


def prefInGroup(student, group):
    lowestPrefScoreMatch = Student_class("None", 0, 99999, False, "")
    firstMatch = True
    for p in student.prefs:
        if p in group:
            if firstMatch is True:
                lowestPrefScoreMatch = p
                firstMatch = False
            elif p.prefScore < lowestPrefScoreMatch.prefScore:
                lowestPrefScoreMatch = p
    return lowestPrefScoreMatch


# return the Student object with the lowest prefScore

# ------------------------------------------------------------------------
# checks to see if a student is already in a group with a preference
# ------------------------------------------------------------------------


def isInSameGroup(student, pref):
    alreadyAssigned = False
# initialize return assuming there is no existing preference in a group

    for searchGroup in Groups:
        pair = [student, pref]
# print "checking same group " + student.name + " with " + pref.name
        if all(x in searchGroup for x in pair):
            # will return True is student and pref are in searchGroup together
            # print "match"
            alreadyAssigned = True
    return alreadyAssigned


# --------------------------------------------
# Output Statitics
# --------------------------------------------


def printStats(students):

    # initialize prefsCount
    prefsCount = []
    for i in range(maxPrefs + 1):
        prefsCount.append(0)

    for s in students:
        prefsMatched = 0
        print ""
        for p in s.prefs:
            if isInSameGroup(s, p) is True:
                prefsMatched += 1

        print s.name + " preferences matched is " + str(prefsMatched)
        prefsCount[prefsMatched] += 1

    print ""
    for p in prefsCount:
        print str(prefsCount.index(p)) + " matches = " + str(p)

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
    l.sort(key=lambda l: (l.prefScore, l.mutualScore), reverse=True)
    return l


def score_students(students):
    for i in students:
        for x in students:
            for y in range(maxPrefs):
                if(x.name == i.prefs[y].name):
                    x.prefScore += 1
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
    for x in range(numOfGroups):  # initialize groups
        Groups.append([])


# -------------------------------
# Assign students to Groups
# -------------------------------
def assign_students(students):
    for s in students:
        # process entire student list

        # if student is NOT assigned
        if s.isAssigned is False:

            # -----------------------------------
            # Determine order to process Groups
            # -----------------------------------
            # determine the Group order to process.
            # Find smallest sized groups
            # if equal then sort by the lowest prefscore
            # groupOrder is a list of (group index, group size, lowest)

            groupOrder = []

# get info for each group
            for x in range(numOfGroups):
                groupOrder.append(["", "", ""])
                groupOrder[x][0] = x
                groupOrder[x][1] = len(Groups[x])
                lowestPref = prefInGroup(s, Groups[x])
                groupOrder[x][2] = lowestPref.prefScore

# sort groupOrder by groupSize then by lowest preference score of a preference
            groupOrder.sort(
                key=lambda l: (l[1], l[2])
            )
# print groupOrder

# -----------------------------------
# Process each group for a student
# -----------------------------------
            tryToPullPreferenceWithStudent = True
# first try to pull a preference with the student into the smallest group
            for i in range(numOfGroups):

                # Condition (G) and (H)
                # check to see if there were no options to pull a preference
                if s.isAssigned is False and \
                        tryToPullPreferenceWithStudent is False:
                    # if not, then need to find another group with a preference
                    if prefInGroup(s, Groups[groupOrder[i][0]]).name != "None":
                        s.isAssigned = True
# mark student as assigned to move to the next student
                        Groups[groupOrder[i][0]].append(s)
# add Student to the group
                        break
# don't process anymore groups
# Condition (F)
                # check if not assigned to skip processing other groups
                if s.isAssigned is False and \
                        tryToPullPreferenceWithStudent is True:

                    # sort preferences by pref-score from highest to lowest
                    s.prefs.sort(key=lambda l: l.prefScore, reverse=True)
# check for Condition (F)
                    pulledPreferenceWithStudent = False
                    for p in s.prefs:
                        # for each preference for a student
                        # if unassigned and prefs-unassigned > 1
                        # pull into group.  Condition (F)
                        if p.isAssigned is False and \
                            p.prefsUnAssigned(numOfGroups, Groups) > 1 and \
                                s.isAssigned is False:
                            s.isAssigned = True
# mark student as assigned to move to the next student
                            p.isAssigned = True
# mark the preference as assigned too
                            Groups[groupOrder[i][0]].append(s)
# add Student to the group
                            Groups[groupOrder[i][0]].append(p)
# add the students preference to the group (pull)
                            pulledPreferenceWithStudent = True
# found a preference to pull into group with student
                    tryToPullPreferenceWithStudent = False
# don't try to pull a preference when processing the remaining groups

                    if pulledPreferenceWithStudent is False:
                        # if couldn't pull in a preference with the student
                        # check to see if there is a preference in the group
                        if prefInGroup(s, Groups[groupOrder[i][0]]).name \
                                != "None":
                            s.isAssigned = True
# mark student as assigned to move to the next student
                            Groups[groupOrder[i][0]].append(s)
# add Student to the group
                            break
        else:
            # if student IS assigned
            alreadyAssignedWithAPreference = False
# need to check multiple cases
# this variable will move to next student after an assignment condition is met
# check to see if already assigned with a preference.  Condition (A)
            for p in s.prefs:
                if isInSameGroup(s, p) is True:
                    alreadyAssignedWithAPreference = True
# pull highest pref-score preference into the same group
            if alreadyAssignedWithAPreference is False:
                s.prefs.sort(key=lambda l: l.prefScore, reverse=True)
# sort prefs by highest pref-score
                for p in s.prefs:
                    if p.isAssigned is False:
                        # check to see if pref is not already assigned
                        gIndex = s.inGroup(Groups)
                        Groups[gIndex].append(p)
# add the students preference to the group (pull).  Condition (B)
                        p.isAssigned = True
# mark is assigned
                        break
# don't check anymore preferences if found one to pull into group

def unassigned_students(stu):
    students = []
    for s in stu:
        if s.isAssigned == False:
            students.append(s)
    print str(len(students)) + " students are unable to be assigned"
    if len(students) != 0:
        print "The following students are unassigned:"
    for i in students:
        print i.name
