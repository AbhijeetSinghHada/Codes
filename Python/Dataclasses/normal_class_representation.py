

# class Student:

#     def __init__(self, name: str, age: int, grade: int, marks: float, ):
#         self.name = name
#         self.age = age
#         self.grade = grade
#         self.marks = marks

#     def __repr__(self):
#         return f"{self.__class__.__name__}(name={self.name}, age={self.age}, grade={self.grade}, marks={self.marks})"


# student1 = Student("Abhi", 19, 12, 90.0)
# student2 = Student("Kittu", 14, 8, 95.0)
# student3 = Student("Raksha", 21, 12, 97.0)
# student4 = Student("Harsh", 19, 8, 91.0)

# print(student1)


class Student:

    def __init__(self, name: str, age: int, grade: int, marks: float):
        self.name = name
        self.age = age
        self.grade = grade
        self.marks = marks

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name}, age={self.age}, grade={self.grade}, marks={self.marks})"

    def __eq__(self, other):
        if not isinstance(other, Student):
            raise NotImplementedError
        return (
            self.grade == other.grade
            and self.marks == other.marks
        )

    def __ge__(self, other):
        if not isinstance(other, Student):
            raise NotImplementedError
        return (
            self.grade >= other.grade
            or self.marks >= other.marks
        )

    def __lt__(self, other):
        if not isinstance(other, Student):
            raise NotImplementedError
        return (
            self.grade < other.grade
            or self.marks < other.marks)


student1 = Student("Abhi", 19, 12, 90.0)
student2 = Student("Kittu", 19, 12, 90.0)
student65 = Student("Kittu", 14, 8, 95.0)
student3 = Student("Raksha", 21, 12, 97.0)
student4 = Student("Harsh", 19, 8, 91.0)
student5 = Student("Udbhav", 191, 12, 90.0)

print(student1)

print(student1 == student2)

