class Student_class:
'''
Student Class code

init: creates a student with 6 arguments
pref_list: prints a student's preferences
prefs_unassigned: counts and returns the number of prefs unassigned for a student
in_group: Returns the Group Index if a student is assigned to any group
'''
    def __init__(student, name, mutual_score, pref_score, is_assigned, prefs):
        student.name = name
        student.mutual_score = mutual_score
        student.pref_score = pref_score
        student.is_assigned = is_assigned
        student.prefs = prefs

    def pref_list(student):
        '''Prints a student's preferences'''
        print(student.name + ": " + student.prefs[0].name + ", "
              + student.prefs[1].name + ", " + student.prefs[2].name + ", "
              + student.prefs[3].name)

    def prefs_unassigned(student, num_of_groups, Groups):
        '''Counts and returns the number of prefs unassigned for a student'''
        pref_count = 0
        for pref in student.prefs:
            for n in range(num_of_groups):
                if pref in Groups[n - 1]:
                    pref_count += 1
        prefs_unassigned = len(student.prefs) - pref_count
        return prefs_unassigned

    def in_group(student, Groups):
        '''Returns the Group Index if a student is assigned to any group'''
        group_index = 99
# check each group to see if the student is in that group
        for g in Groups:
            if student in g:
                group_index = Groups.index(g)
# save and return the Group Index
        return group_index
