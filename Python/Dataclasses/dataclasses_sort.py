from dataclasses import dataclass, field


@dataclass(order=True)
class Student:
    sort_index: int = field(init=False, repr=False)
    name: str
    age: int
    marks: int = field(repr=True)

    def __post_init__(self):
        self.sort_index = self.marks


student_1 = Student('Ram', 12, 93)
student_2 = Student('Shyam', 11, 87)
student_3 = Student('Hari', 12, 99)
student_4 = Student('Gita', 11, 73)
student_5 = Student('Sita', 12, 80)

students = [student_1, student_2, student_3, student_4, student_5]
students.sort(reverse=True)
print(students)
