class Student_class:
    def __init__(self, p, fn, ln):
        self.partner = ""
        self.preferences = []
        self.preference_index = 0
        for x in range(len(p)):
            self.preferences.append(p[x])

        self.first_name = fn
        self.last_name = ln

    def remove_preference_string(self, s):
        self.preferences.remove(s)

    def remove_preference_id(self, id):
        self.preferences.remove(self.preferences[id])
