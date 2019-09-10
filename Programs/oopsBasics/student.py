class Student:
    # We have defined a static or a class level field by globally defining it and assigning it a value.
    major = "CSE"

    def __init__(self, rollNo, name):
        self.rollNo = rollNo
        self.name = name
    

s1 = Student(1, "John")
s2 = Student(2, "Bill")
print(s1.major)
print(s2.major)
print(s1.name)
print(s2.name)

# We can also access a static without making an object as well.
print(Student.major)