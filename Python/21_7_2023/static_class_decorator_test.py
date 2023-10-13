class Student:

    mode = "Online Learning"
    school = "ABC School"
    students = 0

    def __init__(self, name, age, major):
        self.name = name
        self.age = age
        self.major = major
        Student.students += 1

    @classmethod
    def change_mode(cls, mode):
        cls.mode = mode

    @classmethod
    def change_school(cls, school):
        cls.school = school

    @classmethod
    def get_students(cls):
        return cls.students

    def change_mode_for_all(self):
        Student.mode = "Offline Learning"
        return self.mode

    @classmethod
    def split_students(cls, students):
        name, age, major = students.split(",")
        return cls(name, age, major)

    def return_name_age_major(self):
        return f"{self.name} is {self.age} years old and is majoring in {self.major}"


student1 = Student("John", 18, "Computer Science")
student2 = Student("Jane", 19, "Mathematics")
student3 = Student("Jack", 20, "Physics")

print(student1.mode)
print(student2.mode)
print(student3.mode)

student1.change_mode("Offline Learning")
print()

print(student1.mode)
print(student2.mode)
print(student3.mode)


# ===================================

# student1.mode = "Offline Learning"
# print(student1.mode)
# print(student2.mode)
# print(student1.return_name_age_major())
# print(student2.return_name_age_major())

# Student.change_mode("Mix Learning")

# print(student1.mode)
# print(student2.mode)

# print(Student.get_students())

# student3 = Student("Jack", 20, "Physics")
# print(Student.get_students())

# print(student1.students)

# student4 = Student.split_students("Jill,21,Chemistry")
# print(student4.return_name_age_major())
