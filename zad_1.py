from Models.Student import Student
Student1 = Student("Maciek", [60, 70, 80, 90])
Student2 = Student("Jerzy", [20, 30, 40])
print(Student1.is_passed())
print(Student2.is_passed())
