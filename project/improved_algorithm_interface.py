# prototype of group sorting algorithm
"""Contains methods for the Group Matching Algorithm as well as an example of how to run"""
import math
from itertools import repeat

from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, Preference, Student, engine
from Group_class import Group_class
from Student_class import Student_class

APP = Flask(__name__)
ENGINE = create_engine('sqlite:///test.db')
Base.metadata.bind = engine
DBSESSION = sessionmaker(bind=engine)
SESSION = DBSESSION()

# ***********************
# Constants
# ***********************

MAX_PREFS = 3
NUM_OF_GROUPS = 7
# this should be calculated or set by user
max_boys_per_group = 0
max_girls_per_group = 0


# ***********************
# Functions
# ***********************

def print_student_list(students):
    """Prints a list of all the Students"""
    print "Student list size:" + str(len(students))
    for student in students:
        student.prefList()


# ------------------------
# Output All Groups
# ------------------------


def print_all_groups():
    """Prints a list of all the Groups"""
    print "Number of Groups:" + str(len(GROUPS))

    for count in enumerate(GROUPS):
        print ""
        output = "Group " + \
              str(count[0] + \
                  1) + \
              ": " + \
              str(GROUPS[count[0]].boys) + \
              " Boys, " + \
              str(GROUPS[count[0]].girls) + \
              " Girls" + \
              " Total: " + \
              str(len(GROUPS[count[0]]))
        print output
        for student in GROUPS[count[0]]:
            print student.name


def get_all_groups():
    """Returns a List of all the Groups"""
    groups = []
    for count in enumerate(GROUPS):
        group = []
        group.append("Group " + str(count + 1))
        for student in GROUPS[count]:
            group.append(student.name)
        groups.append(group)
    return groups


# --------------------------------------------
# Find lowest matching pref_score in a group
# --------------------------------------------


def pref_in_group(student, group):
    """Finds the preference with the lowest pref_score in a given group"""
    lowest_pref_score_match = Student_class(-1, "None", 0, -1, False, "", "")
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
    """Returns True if the student and preference are in the same group"""
    already_assigned = False
# initialize return assuming there is no existing preference in a group

    for search_group in GROUPS:
        pair = [student, pref]
        if all(x in search_group for x in pair):
            # x is just the comparison variable used
            # will return True is student and pref are in search_group together
            # print "match"
            already_assigned = True
    return already_assigned


# --------------------------------------------
# Output Statitics
# --------------------------------------------


def print_stats(students):
    """Prints a list of statistics on the final Groups"""
    # initialize prefs_count
    prefs_count = []
    for _ in repeat(None, MAX_PREFS + 1):
        prefs_count.append(0)

    no_prefs = 0
    no_pref_students = []
    for student in students:
        total_boys = 0
        total_girls = 0
        prefs_matched = 0
        for preference in student.prefs:
            if is_in_same_group(student, preference) is True:
                prefs_matched += 1

        if not student.prefs:
            no_prefs = no_prefs + 1
        prefs_count[prefs_matched] += 1
        if prefs_matched == 0:
            no_pref_students.append(student.name)

    print ""
    print "0 matches = " + str(prefs_count[0] - no_prefs)
    for preference in prefs_count[1:]:
        print str(prefs_count.index(preference)) + " matches = " + str(preference)

    print""
    group_length = 0
    empty_group = 0
    for group in GROUPS:
        if group == []:
            empty_group += 1
        else:
            group_length += len(group)
    print "The average group size is " + \
        str(group_length / (len(GROUPS) - empty_group))
    print "There are " + str(empty_group) + " empty groups"
    total_boys = 0
    total_girls = 0
    for student in students:
        if student.gender == "Male":
            total_boys += 1
        if student.gender == "Female":
            total_girls += 1

    print "The following students were unable to be assigned"
    for sad_student in no_pref_students:
        print sad_student


# ***********************
# Main Program
# ***********************

# ------------------
# Initialize Data
# ------------------


def get_students():
    """Returns a List of Students and their Preferences from the database"""
    students = []
    student_query = SESSION.query(Student).all()
    preference_query = None
    count = 1
    # makes a list of Student objects from the database
    for student in student_query:
        preference_query = SESSION.query(
            Preference).filter_by(student=student).all()
        students.append(Student_class(student.id, student.name, -1, -1, False,
                                      preference_query, student.gender))
        count = count + 1
    return students


def sort_students(students):
    """Sorts students in order of pref_score first and mutual_score seconed"""
    students.sort(key=lambda students: (students.pref_score,
                                        students.mutual_score), reverse=True)
    return students


def score_students(students):
    """Scores Students for both pref_score and mutual_score"""
    for primary_student in students:
        for comparison_student in students:
            for index in range(MAX_PREFS):
                if not primary_student.prefs:
                    continue
                score_student(primary_student, comparison_student, index)
    return None

def score_student(primary_student, comparison_student, index):
    """Checks if a student is in preference list and scores accordingly"""
    if(comparison_student.name ==
       primary_student.prefs[index].name):
        comparison_student.pref_score += 1
        for secondary_index in range(len(primary_student.prefs)):
            if comparison_student.prefs:
                if(comparison_student.prefs[secondary_index].name ==
                   primary_student.name):
                    comparison_student.mutual_score += 1

def convert_pref_student(students):
    """Converts all of a students preference from Preference to Student"""
    pref = []
    for primary_student in students:
        for comparison_student in students:
            for index in range(MAX_PREFS):
                if primary_student.prefs == []:
                    continue
                if comparison_student.name == primary_student.prefs[index].name:
                    pref.append(comparison_student)
        primary_student.prefs = pref
        pref = []


def concatenate_names(students):
    """Combines a student's first_name and last_name"""
    for student in students:
        for index in range(len(student.prefs)):
            student.prefs[index].name = student.prefs[index].first_name1 + \
                student.prefs[index].last_name1
    return None


# Create Groups
GROUPS = Group_class()


def setup():
    """Creates n empty Groups"""
    for _ in repeat(None, NUM_OF_GROUPS):  # initialize groups
        GROUPS.append(Group_class())


# -------------------------------
# Assign students to Groups
# -------------------------------
def order_groups(student):
    """Creates a group_order list to hold group order information. Will be deprecated soon"""
    group_order = []

# get info for each group
    for count in range(NUM_OF_GROUPS):
        group_order.append(["", "", ""])
        group_order[count][0] = count
        group_order[count][1] = len(GROUPS[count])
        lowest_pref = pref_in_group(student, GROUPS[count])
        group_order[count][2] = lowest_pref.pref_score

# sort group_order by groupSize then by lowest preference score of a preference
    group_order.sort(
        key=lambda l: (l[1], l[2])
    )
    return group_order


def condition_g(
        try_to_pull_preference_with_student,
        student,
        group_order,
        group_index):
    """Assigns a student to the smallest group with a preference
    if the student's preferences all only have 1 preference or less remainingself.
    i.e. Bob is unassigned and 2 of Bob's preferences, Joe and Fred, are also unassigned
    Joe and Fred each have only one unassigned preference.
    Bob will be assigned to the smallest group with a preference."""
    if student.is_assigned is False and \
            try_to_pull_preference_with_student is False:
        # if not, then need to find another group with a preference
        if pref_in_group(student, GROUPS[group_order[group_index][0]]).name != "None":
            student.is_assigned = True
            # mark student as assigned to move to the next student
            GROUPS[group_order[group_index][0]].append(student)
            if student.gender == "Male":
                GROUPS[group_order[group_index][0]].boys += 1
            elif student.gender == "Female":
                GROUPS[group_order[group_index][0]].girls += 1

def condition_f(
        try_to_pull_preference_with_student,
        student,
        group_order,
        group_index):
    """If a student is unassigned and all Groups do not contain a preference,
    the student will then be put into the smallest group
    pulling their highest pref_score preference with them into the group"""
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
                preference.prefsUnAssigned(NUM_OF_GROUPS, GROUPS) > 1 and \
                    student.is_assigned is False:
                student.is_assigned = True
                # mark student as assigned to move to the next student
                preference.is_assigned = True
                # mark the preference as assigned too
                GROUPS[group_order[group_index][0]].append(student)
                # add Student to the group
                if student.gender == "Male":
                    GROUPS[group_order[group_index][0]].boys += 1
                elif student.gender == "Female":
                    GROUPS[group_order[group_index][0]].girls += 1

                GROUPS[group_order[group_index][0]].append(preference)
                # add the students preference to the group (pull)
                if preference.gender == "Male":
                    GROUPS[group_order[group_index][0]].boys += 1
                elif preference.gender == "Female":
                    GROUPS[group_order[group_index][0]].girls += 1

                pulled_preference_with_student = True
                # found a preference to pull into group with student
        try_to_pull_preference_with_student = False
        # don't try to pull a preference when processing the remaining groups
        condition_d(pulled_preference_with_student,
                    student, group_order, group_index)


def condition_d(
        pulled_preference_with_student,
        student,
        group_order,
        group_index):
    """Assigns a student to the smallest group with a preference"""
    if pulled_preference_with_student is False:
        # if couldn't pull in a preference with the student
        # check to see if there is a preference in the group
        if pref_in_group(student, GROUPS[group_order[group_index][0]]).name \
                != "None":
            student.is_assigned = True
            GROUPS[group_order[group_index][0]].append(student)
            if student.gender == "Male":
                GROUPS[group_order[group_index][0]].boys += 1
            elif student.gender == "Female":
                GROUPS[group_order[group_index][0]].girls += 1


def condition_a_b(student):
    """If a student is already assigned but does not have a preference in their group,
    then they will pull in the highest pref_score preference into their group.
    If a student is already in a group with a preference, do nothing"""
    already_assigned_with_a_preference = False
    for preference in student.prefs:
        if is_in_same_group(student, preference) is True:
            already_assigned_with_a_preference = True
            # pull highest pref-score preference into the same group
    if already_assigned_with_a_preference is False:
        student.prefs.sort(key=lambda l: l.pref_score, reverse=True)
        # sort prefs by highest pref-score
        for preference in student.prefs:
            g_index = student.inGroup(GROUPS)
            if preference.is_assigned is False:
                # check to see if pref is not already assigned
                GROUPS[g_index].append(preference)
                # add the students preference to the group (pull).  Condition (B)
                preference.is_assigned = True
                if preference.gender == "Male":
                    GROUPS[g_index].boys += 1
                elif preference.gender == "Female":
                    GROUPS[g_index].girls += 1

                    # mark is assigned
                break


def assign_students(students):
    """Runs the logic behind all the above Conditions that assign students
    Will also try to balance out groups based on gender"""
    print "Max Boys Per Group: " + str(max_boys_per_group)
    print "Max Girls Per Group: " + str(max_girls_per_group)

    for student in students:
        # process entire student list
        # if student is NOT assigned
        if student.is_assigned is False:
            group_order = order_groups(student)
# -----------------------------------
# Process each group for a student
# -----------------------------------
            try_to_pull_preference_with_student = True
            # first try to pull a preference with the student into the smallest group
            for group_index in range(NUM_OF_GROUPS):
                # Condition (G) and (H)
                # check to see if there were no options to pull a preference
                condition_g(try_to_pull_preference_with_student,
                            student, group_order, group_index)
                # add Student to the group
                if student.is_assigned is True:
                    break
                # don't process anymore groups
                # Condition (F)
                condition_f(try_to_pull_preference_with_student,
                            student, group_order, group_index)

                if student.is_assigned is True:
                    break
        else:
            condition_a_b(student)


def assign_no_prefs(students):
    """If a student has no preferences,
    they will be assigned to the smallest group"""
    for student in students:
        if student.is_assigned is False:
            group_order = order_groups(student)
            GROUPS[group_order[0][0]].append(student)
            student.is_assigned = True
            if student.gender == "Male":
                GROUPS[group_order[0][0]].boys += 1
            elif student.gender == "Female":
                GROUPS[group_order[0][0]].girls += 1


def unassigned_students(stu):
    """Checks to see if any students were unable to be assigned"""
    students = []
    for student in stu:
        if not student.is_assigned:
            students.append(student)
    print str(len(students)) + " students are unable to be assigned"
    if students:
        print "The following students are unassigned:"
    for student in students:
        print student.name


def count_gender(students):
    """Counts the amount of boys and girls in the group of Students"""
    global max_boys_per_group
    global max_girls_per_group
    boys = 0
    girls = 0

    for student in students:
        if student.gender == "Male":
            boys += 1
        elif student.gender == "Female":
            girls += 1

    max_boys_per_group = math.floor(boys / NUM_OF_GROUPS) + 1
    max_girls_per_group = math.floor(girls / NUM_OF_GROUPS) + 1


TEST = get_students()
# concatenate_names(TEST)
score_students(TEST)
sort_students(TEST)
convert_pref_student(TEST)
setup()
count_gender(TEST)
assign_students(TEST)
assign_no_prefs(TEST)
print_all_groups()
unassigned_students(TEST)
print_stats(TEST)
