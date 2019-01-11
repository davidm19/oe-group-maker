class Student_class:
    def __init__(self, p, fn, ln, pnum):
        self.preferences = []
        if(p != None):
            for x in range(len(p)):
                self.preferences.append(p[x])

        self.first_name = fn
        self.last_name = ln
        self.name = self.first_name + self.last_name
        self.pref_score = 0
        self.mutual_score = 0
        self.is_assigned = False
        self.group = -1
        self.conditionA = False
        self.remaining = pnum
        self.rdefault = pnum
