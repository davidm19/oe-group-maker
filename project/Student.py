class Student:
    def __init__(p, fn, ln):
        self.partner = ""
        self.preferences = ""
        for x in p:
            self.preferences.append(p[x])

        self.first_name = fn
        self.last_name = ln

    def remove_preference_string(s):
        self.preferences.remove(s)

    def remove_preference_id(id):
        del self.preferences[id]
