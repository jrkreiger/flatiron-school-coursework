class School:
    def __init__(self, name, roster=None):
        self.name = name
        self.roster = {}
        
    def add_student(self, student_name, grade_level):
        if grade_level in self.roster:
            self.roster[grade_level].append(student_name)
        else:
            self.roster[grade_level] = [student_name]
    def grade(self, grade):
        return self.roster[grade]
    
    def sort_roster(self):
        sorted_roster = self.roster
        for grade in sorted_roster:
            sorted_roster[grade].sort()
        return sorted_roster
       
