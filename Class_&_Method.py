class StudentRecord:
    stdEntries = 0
    def __init__(self, name, dept, cgpa):
        self.name = name
        self.dept = dept
        self.cgpa = cgpa
        StudentRecord.stdEntries += 1

    def display(self):
        print(self.name+" is from "+self.dept+" department and "+"scored", self.cgpa, "cgpa")

std1 = StudentRecord("Seema", "ECE", 8.9)
std2 = StudentRecord("Raman", "CSE", 9.5)
std1.display()
std2.display()
print("Total entries: ", StudentRecord.stdEntries)
