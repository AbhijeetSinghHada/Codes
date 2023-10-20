from dataclasses import dataclass, field, asdict, astuple
from typing import NamedTuple


@dataclass(order=True, unsafe_hash=True)
class Student:
    index: int = field(init=False, repr=False)
    name: str = field(compare=False)
    age: int
    grade: int
    marks: float

    def __post_init__(self):
        self.index = self.age


student1 = Student("Test1", 19, 12, 90.0)
student2 = Student("Test2", 14, 8, 95.0)
student3 = Student("Test3", 21, 12, 97.0)
student4 = Student("Test4", 19, 8, 91.0)
student5 = Student("Test5", 19, 12, 90.0)

print(student1 == student5)

print(student1.__hash__())
student1.age = 20
print(student1.__hash__())



student = NamedTuple("student", [("name",str) , ("age", int), ("grade", int), ("marks", float)])
teacher = NamedTuple("teacher", [("name",str) , ("age", int), ("height", int), ("salary", float)])

student6 = student("Test6", 19, 12, 90.0)
student7 = teacher("Test6", 19, 12, 90.0)

print(student6 == student7)
