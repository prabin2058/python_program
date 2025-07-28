class Student:
    def __init__(self, name, grade="Not Assigned"):
        self.name = name
        self.grade = grade

obj = Student("Prabin", "A")

print(obj.name)
print(obj.grade)

