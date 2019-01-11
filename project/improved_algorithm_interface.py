# prototype of group sorting algorithm
import sys #to be able to sys.exit() to stop at break point for debugging
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
from Student_class import Student_class

app = Flask(__name__)
engine = create_engine('sqlite:///database.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

#***********************
# Constants
#***********************

maxPrefs = 4
numOfGroups = 6  #this should be calculated or set by user




#***********************
# Functions
#***********************

#------------------------
# Output student list
#------------------------
def printStudentList():
    print("Student list size:" + str(len(students)))
    for x in students:
        x.prefList()

#------------------------
# Output All Groups
#------------------------
def printAllGroups():
    print("Number of Groups:" + str(len(Groups)))

    for x in range(len(Groups)):
        print("")
        print("Group " + str(x+1))
        print("_______________")
        for y in Groups[x]:
            #print(y.name + " MutualScore=" + str(y.mutualScore) + " PrefScore=" + str(y.prefScore))
            print(y.name)

#--------------------------------------------
# Find lowest matching prefScore in a group
#--------------------------------------------
def prefInGroup(student, group):
    lowestPrefScoreMatch = Student_class("None",0,99999,False,"")
    firstMatch = True
    for p in student.prefs:
        #print("checking: " + p.name )
        if p in group:
            #print("found a match for student: " + student.name + " with "+ p.name +" who has a prefScore of " + str(p.prefScore))
            if firstMatch == True:
                lowestPrefScoreMatch = p
                firstMatch = False
            elif p.prefScore < lowestPrefScoreMatch.prefScore:
                lowestPrefScoreMatch = p

    #print "Lowest matching prefScore in group is " +str(lowestPrefScoreMatch.name) + " with a prefscore of " + str(lowestPrefScoreMatch.prefScore)

    return lowestPrefScoreMatch  #return the Student object with the lowest prefScore

#------------------------------------------------------------------------
# checks to see if a student is already in a group with a preference
#------------------------------------------------------------------------
def isInSameGroup(student, pref):
    alreadyAssigned = False #initialize return assuming there is no existing preference in a group

    for searchGroup in Groups:
        pair = [student, pref]
        #print "checking same group " + student.name + " with " + pref.name
        if all(x in searchGroup for x in pair):   #will return True is student and pref are in searchGroup together
            #print "match"
            alreadyAssigned = True
    return alreadyAssigned

#--------------------------------------------
# Output Statitics
#--------------------------------------------
def printStats(students):

    #initialize prefsCount
    prefsCount=[]
    for i in range(maxPrefs+1):
        prefsCount.append(0)

    for s in students:
        prefsMatched=0
        print ""
        for p in s.prefs:
            if isInSameGroup(s, p) == True:
                    prefsMatched += 1

        print s.name + " preferences matched is " + str(prefsMatched)
        prefsCount[prefsMatched] += 1

    print ""
    for p in prefsCount:
        print str(prefsCount.index(p)) + " matches = " + str(p)

#***********************
# Main Program
#***********************

#------------------
# Initialize Data
#------------------

def get_students():
    students = []
    temp1 = session.query(Student).all()
    temp2 = None
    temp3 = []
    count = 1;
    #makes a list of Student objects from the database
    for i in temp1:
        temp2 = session.query(Preference).filter_by(student_id = count).all()
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
                #print("%s --- %s" % (x.name, i.preferences[y].name))
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
<<<<<<< HEAD
#create list of students first without preferences because preferences refer to objects not yet defined

students=get_students()
concatenate_names(students)
score_students(students)
sort_students(students)
print(students[0].prefs[0].name)
convert_pref_student(students)
print(students[0].prefs)
'''
students.append (Student("Jack",2,9,False,""))
students.append (Student("Fred",2,9,False,""))
students.append (Student("Tej",0,9,False,""))
students.append (Student("Bob",3,7,False,""))
students.append (Student("Frank",1,7,False,""))
students.append (Student("Manny",1,6,False,""))
students.append (Student("Jonathan",0,6,False,""))
students.append (Student("Magic",0,5,False,""))
students.append (Student("Jordan",1,4,False,""))
students.append (Student("Cooper",1,4,False,""))
students.append (Student("Rambus",1,4,False,""))
students.append (Student("Patrick",0,4,False,""))
students.append (Student("Fisher",0,4,False,""))
students.append (Student("Wilt",0,4,False,""))
students.append (Student("Kareem",0,3,False,""))
students.append (Student("Kobe",0,3,False,""))
students.append (Student("Shaq",0,3,False,""))
students.append (Student("Lebron",0,3,False,""))
students.append (Student("Curry",0,3,False,""))
students.append (Student("Reggie",0,3,False,""))
students.append (Student("Worthy",0,3,False,""))
students.append (Student("Moe",1,2,False,""))
students.append (Student("Jerry",1,2,False,""))
students.append (Student("Joe",0,2,False,""))
students.append (Student("Nev",0,2,False,""))
students.append (Student("James",0,2,False,""))
students.append (Student("Byron",0,2,False,""))
students.append (Student("Horry",0,2,False,""))
students.append (Student("Gasol",0,2,False,""))
students.append (Student("Durant",0,1,False,""))

#add prefs to list of students
students[0].prefs = [students[5], students[3], students[1], students[11]]
students[1].prefs = [students[11], students[3], students[0], students[12]]
students[2].prefs = [students[11], students[3], students[18], students[19]]
students[3].prefs = [students[1], students[0], students[7], students[10]]
students[4].prefs = [students[3], students[5], students[20], students[26]]
students[5].prefs = [students[25], students[4], students[16], students[27]]
students[6].prefs = [students[1], students[4], students[0], students[16]]
students[7].prefs = [students[11], students[16], students[14], students[25]]
students[8].prefs = [students[7], students[22], students[24], students[23]]
students[9].prefs = [students[10], students[21], students[15], students[18]]
students[10].prefs = [students[28], students[0], students[12], students[3]]
students[11].prefs = [students[3], students[4], students[8], students[21]]
students[12].prefs = [students[13], students[5], students[2], students[0]]
students[13].prefs = [students[10], students[2], students[1], students[29]]
students[14].prefs = [students[13], students[12], students[2], students[5]]
students[15].prefs = [students[0], students[1], students[19], students[2]]
students[16].prefs = [students[4], students[1], students[18], students[28]]
students[17].prefs = [students[14], students[23], students[5], students[4]]
students[18].prefs = [students[26], students[8], students[20], students[1]]
students[19].prefs = [students[7], students[9], students[10], students[8]]
students[20].prefs = [students[6], students[2], students[12], students[22]]
students[21].prefs = [students[6], students[2], students[9], students[7]]
students[22].prefs = [students[6], students[17], students[8], students[15]]
students[23].prefs = [students[4], students[6], students[13], students[9]]
students[24].prefs = [students[2], students[6], students[19], students[14]]
students[25].prefs = [students[1], students[2], students[15], students[6]]
students[26].prefs = [students[27], students[5], students[0], students[20]]
students[27].prefs = [students[17], students[3], students[0], students[13]]
students[28].prefs = [students[9], students[4], students[0], students[24]]
students[29].prefs = [students[1], students[2], students[7], students[17]]
'''
=======
>>>>>>> 366805d8ff0f363b7aea0b8b5888ad608501c78a

#Create Groups
Groups = []
def setup():
    for x in range(numOfGroups):  #initialize groups
        Groups.append([])


#-------------------------------
# Assign students to Groups
#-------------------------------
def assign_students(students):
    for s in students:   #process entire student list
        print ""
        print "Processing " + s.name + "..."

        #if student is NOT assigned
        if s.isAssigned == False:

            #-----------------------------------
            # Determine order to process Groups
            #-----------------------------------
            #determine the Group order to process.  Find smallest sized groups and if equal then sort by the lowest prefscore
            #groupOrder is a list of (group index, group size, lowest)

            groupOrder = []

            # get info for each group (ie size and the lowest matching pref score if there is one in the group)
            for x in range(numOfGroups):
                groupOrder.append(["","",""])
                groupOrder[x][0]=x
                groupOrder[x][1]=len(Groups[x])
                lowestPref=prefInGroup(s,Groups[x])
                groupOrder[x][2]=lowestPref.prefScore

            #sort groupOrder by groupSize then by lowest preference score of a preference if there is a preference at all
            groupOrder.sort(
                key = lambda l: (l[1], l[2])
                )
            #print groupOrder

            #-----------------------------------
            # Process each group for a student
            #-----------------------------------
            tryToPullPreferenceWithStudent = True #first try to pull a preference with the student into the smallest group
            for i in range(numOfGroups):

                #Condition (G) and (H)
                if s.isAssigned == False and tryToPullPreferenceWithStudent == False:  #check to see if there were no options to pull a preference into the same groupself.
                        #... so if not, then need to find another group with a preference to assign this person
                    print "Processing group " + str(groupOrder[i][0])
                    if prefInGroup(s,Groups[groupOrder[i][0]]).name != "None":
                        s.isAssigned = True  #mark student as assigned to move to the next student
                        Groups[groupOrder[i][0]].append(s)  #add Student to the group
                        print "(G)(H)" + "Adding " + s.name + " to Group " + str(groupOrder[i][0])
                        break #don't process anymore groups

                #Condition (F)
                if s.isAssigned == False and tryToPullPreferenceWithStudent == True:   #check if not assigned to skip processing other groups once assigned
                    print "Processing group " + str(groupOrder[i][0])

                    s.prefs.sort(key = lambda l: l.prefScore, reverse=True )  # sort preferences by pref-score from highest to lowest

                    #print s.name + "preferences checking..."
                    #print s.prefs[0].name + " " + str(s.prefs[0].prefScore)
                    #print s.prefs[1].name + " " + str(s.prefs[1].prefScore)
                    #print s.prefs[2].name + " " + str(s.prefs[2].prefScore)
                    #print s.prefs[3].name + " " + str(s.prefs[3].prefScore)

                    #check for Condition (F)
                    pulledPreferenceWithStudent=False
                    for p in s.prefs:  # for each preference for a student
                        #print p.name + " " + str(p.isAssigned) + " " + str(p.prefsUnAssigned())

                        #if unassigned and prefs-unassigned > 1 then pull into group.  Condition (F)
                        if p.isAssigned == False and p.prefsUnAssigned(numOfGroups, Groups) > 1 and s.isAssigned == False:
                            s.isAssigned = True  #mark student as assigned to move to the next student
                            p.isAssigned = True  #mark the preference as assigned too
                            Groups[groupOrder[i][0]].append(s)  #add Student to the group
                            Groups[groupOrder[i][0]].append(p)  #add the students preference to the group (pull)
                            pulledPreferenceWithStudent = True #found a preference to pull into group with student
                            print "(F) Pulling " + p.name + " into Group " + str(groupOrder[i][0]) + " with " + s.name
                    tryToPullPreferenceWithStudent = False #don't try to pull a preference when processing the remaining groups

                    if pulledPreferenceWithStudent == False:  #if couldn't pull in a preference with the student then check to see if there is a preference in the group already
                        if prefInGroup(s,Groups[groupOrder[i][0]]).name != "None":
                            s.isAssigned = True  #mark student as assigned to move to the next student
                            Groups[groupOrder[i][0]].append(s)  #add Student to the group
                            print "(D)" + "Adding " + s.name + " to Group " + str(groupOrder[i][0])
                            break #don't process anymore groups


        else:  #if student IS assigned


            alreadyAssignedWithAPreference = False #need to check multiple cases, so this variable will move to next student after an assignment condition is met

            #check to see if already assigned with a preference.  Condition (A)
            for p in s.prefs:
                if isInSameGroup(s, p) == True:
                    print "(A) " + s.name + " is assigned in the same group as " + p.name
                    alreadyAssignedWithAPreference = True

            #pull highest pref-score preference into the same group
            if alreadyAssignedWithAPreference == False:
                s.prefs.sort(key = lambda l: l.prefScore, reverse=True )  #sort prefs by highest pref-score
                for p in s.prefs:
                    if p.isAssigned == False:   #check to see if pref is not already assigned to another group
                        gIndex = s.inGroup(Groups)
                        Groups[gIndex].append(p)  #add the students preference to the group (pull).  Condition (B)
                        p.isAssigned = True  #mark is assigned
                        print "(B) " + p.name + " was pulled into group with " + s.name
                        break #don't check anymore preferences if found one to pull into group

#create list of students first without preferences because preferences refer to objects not yet defined
asdf=get_students()
concatenate_names(asdf)
score_students(asdf)
sort_students(asdf)
convert_pref_student(asdf)
setup()
assign_students(asdf)
printAllGroups()
printStats(asdf)
