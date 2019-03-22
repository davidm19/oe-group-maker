class Student_class_no_gender:
  def __init__(student, name, mutual_score, pref_score, is_assigned,prefs):
    student.name = name
    student.mutual_score = mutual_score
    student.pref_score = pref_score
    student.is_assigned = is_assigned
    student.prefs = prefs

  #--------------------------------------------
  #Utility to print a students preferences
  #--------------------------------------------
  def prefList(student):
    print(student.name + ": " + student.prefs[0].name + ", " +student.prefs[1].name + ", " +student.prefs[2].name+ ", " +student.prefs[3].name)

  #--------------------------------------------
  #Counts the number of preferences Unassigned for a student
  #--------------------------------------------
  def prefsUnAssigned(student, numOfGroups, Groups):
    # Count the number of preferences already assigned for a student
    prefcount = 0
    for pref in student.prefs:
      for n in range(numOfGroups):
          if pref in Groups[n-1]:
              prefcount += 1
    prefsunassigned = len(student.prefs) - prefcount
    return prefsunassigned

  #--------------------------------------------
  #Returns the Group Index if a student is assigned to any group
  #--------------------------------------------
  def inGroup(student, Groups):
    groupIndex = 99

    #check each group to see if the student is in that group
    for g in Groups:
        if student in g:
            groupIndex = Groups.index(g)  #save and return the Group Index

    return groupIndex
