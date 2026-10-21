class Student:
    def __init__(self,name, marks):
        self.name = name
        self.marks = marks
    def is_passed()->bool:
        return sum(self.marks)/len(self.marks)>50
#jestem kuba i jestem gupi
Student1 = Student("Maciek",[60,70,80,90])
Student2 = Student("Jerzy",[20,30,40])
print(Student1.is_passed())
print(Student2.is_passed())