class Student_class:
  def __init__(student, name, mutualScore, prefScore, isAssigned,prefs):
    student.name = name
    student.mutualScore = mutualScore
    student.prefScore = prefScore
    student.isAssigned = isAssigned
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
