

class Student:

    def __init__(self, name: str, age: int, grade: int, marks: float, ):
        self.name = name
        self.age = age
        self.grade = grade
        self.marks = marks

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name}, age={self.age}, grade={self.grade}, marks={self.marks})"


student1 = Student("Abhi", 19, 12, 90.0)
student2 = Student("Kittu", 14, 8, 95.0)
student3 = Student("Raksha", 21, 12, 97.0)
student4 = Student("Harsh", 19, 8, 91.0)

print(student1)
