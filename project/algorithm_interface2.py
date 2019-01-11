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

'''
selects students from grade level
'''
# def getstudents_by_gradelevel(gradeLevel):
#     return session.query(Student).filter_by(grade=gradeLevel).all()

'''
selects students from trip ID
'''
# def getstudents_by_tripID(tripID):
#     return session.query(Student).filter_by(id = tripID).all()

# def getpreferences_by_studentID(studID):
#     return session.query(Preference).filter_by(id = studID).all()

'''
finds tentative parteners for each person using student ID
'''
def temp_partner_id_db(student, stuID):
    student.partner = session.query(Preference).filter_by(student_id = stuID).filter_by(priority = 1).one().name
    #student.partner = student.preferences[0]
    return student.partner

'''
finds tentative parteners for each person using student preference list
'''
def temp_partner_id(student):
    #print(student.preferences)
    if (student.preference_index >= len(student.preferences)):
        student.partner = Preference(name = 'NO MATCH')
    else:
        student.partner = student.preferences[student.preference_index]
        student.preference_index = student.preference_index + 1

    return student.partner

def remove_extraneous_preferences(student):
    i = 1
    while i < student.preference_index:
        student.remove_preference_id(i)
        i += 1

'''
finds tentative parteners for each person using student last name
'''
def temp_partner_last_name(student, stuLN):
    student.partner = session.query(Preference).filter_by(last_name = stuLN).one().name
    return student.partner

'''
eliminates partners given a preference string
'''
# def remove_one_student(student, preference):
#     student.remove_preference_string(preference)

'''
eliminates students in a lower preference rating compared to the given
'''
# def remove_lesser_students(student, preference):
#     time_to_delete = False
#     for x in student.preferences:
#         if time_to_delete == True:
#             student.remove_preference_string(preference)
#         if preference == student.prefernces[x]:
#             time_to_delete = True
#
# def setup(num):
#     for x in range(num):
#         students.append(Student())

'''
deletes preferences lower than the "most preferred"... step 2 of the irving algorithm
'''
def remove_lowpriority_pairs(student, session):
#find first preference (student y) of given student (student x)
    # preferences = session.query(Preference).filter_by(student_id = student.id).all()
    preferences = session.query(Preference).filter_by(priority = 5)
    #print(preferences)
    first_priority = preferences.filter_by(student_id = student.id).one()
    student_to_keep = session.query(Student).filter_by(first_name = first_priority.name).one()
    print("\n")
    print("student to keep")
    print(student_to_keep.first_name)
    print("student to keep prefs")
    student_tkPrefs = session.query(Preference).filter_by(student_id = student_to_keep.id).all()
    for stud in student_tkPrefs:
        print(stud.name)
    student_tk = Student_class(student_tkPrefs, student_to_keep.first_name, student_to_keep.last_name)
#find student x in student y's preference list
    x = 0
    i = len(student_tkPrefs)
    for stud in student_tk.preferences:
        x += 1
        if student.first_name == stud.name:
            k = stud.priority
            print("delete preferences after: " + stud.name)
            while(x < i+1):
                k = k-1
                preference_to_del = session.query(Preference).filter_by(student_id = student_to_keep.id)
                if preference_to_del.filter_by(priority = k).one_or_none() is not None:
                    preference = preference_to_del.filter_by(priority = k).one()
                    print("preference(s) to delete: " + preference.name)
                    print("deleting: " + preference.name + " from: ")
                    print(preference.student_id)
                    session.delete(preference)
                    id_pref_to_del = preference.id
                    name_of_pref = preference.name
#remove students (z) in student y's preference list that have lower priority than student x
#remove student y from students z's lists
                    student_tbr = session.query(Student).filter_by(first_name = name_of_pref).one()
                    student_remove = Student_class(session.query(Preference).filter_by(student_id = student_tbr.id).all(), student_tbr.first_name, student_tbr.last_name)
                    for stud in student_remove.preferences:
                        if stud.name == student_to_keep.first_name:
                            studs_to_del = session.query(Preference).filter_by(name = student_to_keep.first_name)
                            if studs_to_del.filter_by(student_id = student_tbr.id).one_or_none() is not None:
                                studs_to_del = studs_to_del.filter_by(student_id = student_tbr.id).one()
                                print("deleting: " + studs_to_del.name + " from ")
                                print(studs_to_del.student_id)
                                session.delete(studs_to_del)
                                session.commit()
                x+=1

def make_stable_pairs(student, session):
    stable_groups = []
    student_prefs = session.query(Preference).filter_by(student_id = student.id).all()
    if len(student_prefs) == 1:
        pref_student = session.query(Student).filter_by(first_name = student_prefs.name).one()
        pref_student_pref = session.query(Preference).filter_by(student_id = pref_student.id)
        pref_student_pref = pref_student_pref.filter_by(priority = 3).one()
        if student_prefs.name == pref_student_pref.name:
            stable_groups.append([student_prefs.name, pref_student_pref.name])
    return stable_groups

#input student is student x
#first_priority is same student as student_to_keep and student_tk (student y)
#student_to_be_removed is same student as student_tbr and student_remove (student z)

# def cycle_finder(students):
#     i = 0;
#     while True:
#         p.append(students[i])
#         q.append(students[i].preferences[-1])
#         i += 1
#
# def check_for_mutual_pref(student, session):
#     preferences = session.query(Preference).filter_by(student_id = student.id).all()
#     students_to_remove = []
#     if len(preferences) > 2:
#         k = 0
#         for pref in preferences:
#             x = 0
#             student_mutual = session.query(Student).filter_by(first_name = pref.name).one()
#             mutual_prefs = session.query(Preference).filter_by(student_id = student_mutual.id).all()
#             for pref in mutual_prefs:
#                 if student_mutual.first_name == student.first_name:
#                     x += 1
#                     k += 1
#             if x == 0:
#                 student_to_remove = session.query(Preference).filter_by(name = student_mutual.first_name)
#                 student_to_remove = student_to_remove.filter_by(student_id = student.id).one()
#                 students_to_remove.append(student_to_remove)
#         if k > 0:
#             for pref in students_to_remove:
#                 session.delete(pref)
#                 session.commit()
#         if k == 0:
#             last_pref_remove = session.query(Preference).filter_by(priority = 3)
#             l_p_r = last_pref_remove.filter_by(student_id = student.id).one()
#             session.delete(l_p_r)
#             session.commit()




'''
exports the final list (currently returns doubles, this is a bad thing and will be fixed)
'''
def export_scores(students):
    list = []
    for x in students:
        list.append("%s - %s - %s" % (x.pref_score, x.mutual_score, x.first_name))

    return list

def export_list_names(grp):
    list = []
    final_list = []
    for x in grp:
        del x[0]
    for x in grp:
        for y in range(len(x)):
            list.append(x[y].name)
        final_list.append(list)
        list = []
    return final_list

def export_list_preferences(students):
    list = []
    student_pref = ""
    for x in students:
        student_pref = x.first_name + " --- "
        for i in range(len(x.preferences)):
            student_pref = student_pref + "%s, " % (x.preferences[i].name)
        list.append(student_pref)

    return list

'''sp1 = ["Bob", "Joe", "Fred"]
sp2 = session.query(Preference).filter_by(student_id = 2).all()
sp3 = []
for i in sp2:
    sp3.append(i.name)
s1 = Student_class(sp3, "Ryan", "Hom")
print(temp_partner_id(s1))

print(sp3)'''

'''
Janky first step in the alg. Will put into a method
'''
'''
Gets all students from the database
'''
def get_students():
    students = []
    temp1 = session.query(Student).all()
    temp2 = None
    temp3 = []
    count = 1;
    #makes a list of Student objects from the database
    for i in temp1:
        temp2 = session.query(Preference).filter_by(student_id = count).all()
        students.append(Student_class(temp2, i.first_name, i.last_name, len(temp2)))
        count = count + 1
    for i in students:
        if(i.remaining != 4):
            print("PANIC")
    return students

def convert_pref_student(students):
    pref = []
    for i in students:
        for x in students:
            for y in range(4):
                if(x.name == i.preferences[y].name):
                    pref.append(x)
        i.preferences = pref
        pref = []

def sort_students(l):
    l.sort(key=lambda l: (l.pref_score, l.mutual_score), reverse=True)
    return l

def score_students(students):
    for i in students:
        for x in students:
            for y in range(4):
                #print("%s --- %s" % (x.name, i.preferences[y].name))
                if(x.name == i.preferences[y].name):
                    x.pref_score += 1
                    for a in range(len(i.preferences)):
                        if(x.preferences[a].name == i.name):
                            x.mutual_score += 1

    return None

def concatenate_names(students):
    for i in students:
        for y in range(len(i.preferences)):
            i.preferences[y].name = i.preferences[y].first_name1 + i.preferences[y].last_name1
    return None

groups = list()
def setup(ng):
    for i in range(ng):
        item = [i]
        groups.append(item)
    print(groups)
    print("%s groups made!" % ng)

def assign_students(students, ng):
    breaking = False;
    for i in students:
        tryToPullPreferenceWithStudent = True #first try to pull a preference with the student into the smallest group
        #print("first loop")
        #Updates the amount of remaining unassigned Preferences for each Student
        for q in students:
            q.remaining = q.rdefault
        for q in students:
            for w in q.preferences:
                if(w.is_assigned == True):
                    q.remaining -= 1
        #Checks if any of i's preferences are in a group
        if(i.is_assigned == True):
            alreadyAssignedWithAPreference = False #need to check multiple cases, so this variable will move to next student after an assignment condition is met

            #check to see if already assigned with a preference.  Condition (A)
            for p in i.preferences:
                if i.group == p.group:
                    print "(A) " + i.name + " is assigned in the same group as " + p.name
                    alreadyAssignedWithAPreference = True

            #pull highest pref-score preference into the same group
            if alreadyAssignedWithAPreference == False:
                for p in i.preferences:
                    if p.is_assigned == False:   #check to see if pref is not already assigned to another group
                        groups[i.group].append(p)  #add the students preference to the group (pull).  Condition (B)
                        p.is_assigned = True  #mark is assigned
                        p.group = i.group
                        print "(B) " + p.name + " was pulled into group with " + i.name
                        break #don't check anymore preferences if found one to pull into group

        if(i.is_assigned == False):
            group_lengths = list()
            temp = min(groups, key=len)
            pulledPreferenceWithStudent=False
            for x in range(1):
                #print p.name + " " + str(p.isAssigned) + " " + str(p.prefsUnAssigned())
                for p in i.preferences:  # for each preference for a student
                    #if unassigned and prefs-unassigned > 1 then pull into group.  Condition (F)
                    if p.is_assigned == False and p.remaining > 1 and i.is_assigned == False:
                        i.is_assigned = True  #mark student as assigned to move to the next student
                        p.is_assigned = True  #mark the preference as assigned too
                        i.group = temp[0]
                        p.group = temp[0]
                        temp.append(i)  #add Student to the group
                        temp.append(p)  #add the students preference to the group (pull)
                        pulledPreferenceWithStudent = True #found a preference to pull into group with student
                        print "(F) Pulling " + p.name + " into Group " + str(temp[0]) + " with " + i.name
                    tryToPullPreferenceWithStudent = False #don't try to pull a preference when processing the remaining groups

                    '''if pulledPreferenceWithStudent == False and i.preferences:  #if couldn't pull in a preference with the student then check to see if there is a preference in the group already
                        sorted_groups = sorted(groups, key=len)
                        for g in sorted_groups:
                            for p in i.preferences:
                                if p in g:
                                    i.is_assigned = True  #mark student as assigned to move to the next student
                                    groups[p.group].append(i)  #add Student to the group
                                    print "(D)" + "Adding " + i.name + " to Group " + str(p.group)
                                    break #don't process anymore groups
                            break'''
                #Condition (G) and (H)
                if i.is_assigned == False and tryToPullPreferenceWithStudent == False:  #check to see if there were no options to pull a preference into the same groupself.
                        #... so if not, then need to find another group with a preference to assign this person
                    #print "Processing group " + str(temp[0])
                    preferences = sorted(i.preferences, key=lambda l: (i.pref_score, i.mutual_score))
                    sorted_groups = sorted(groups, key=len)
                    for p in preferences:
                        for g in sorted_groups:
                            if p in g:
                                i.is_assigned = True  #mark student as assigned to move to the next student
                                i.group = p.group
                                groups[p.group].append(i)  #add Student to the group
                                print "(G)(H)" + "Adding " + i.name + " to Group " + str(p.group)
                                break #don't process anymore groups
                        break
                    break


asdf = get_students()
concatenate_names(asdf)
score_students(asdf)
print(export_scores(sort_students(asdf)))
convert_pref_student(asdf)
setup(4)
assign_students(asdf, 4)
print(export_list_names(groups))
#print(asdf[13].name)
#print(asdf[13].preferences[0].name)
#print(asdf[13].preferences[1].name)
#print(asdf[13].preferences[2].name)
#print(asdf[13].preferences[3].name)
