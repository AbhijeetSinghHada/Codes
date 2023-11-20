from dataclasses import dataclass, field, asdict, astuple, fields
from typing import NamedTuple


@dataclass(order=True)
class Student:
    index: int = field(init=False, repr=False)
    name: str = field(compare=False)
    age: int
    grade: int
    marks: float = 100

    def __post_init__(self):
        self.index = self.age


student1 = Student("Test1", 19, 12, 90.0)
student2 = Student("Test2", 14, 8, 95.0)
student3 = Student("Test3", 21, 12, 97.0)
student4 = Student("Test4", 19, 8, 91.0)
student5 = Student("Test5", 19, 12)

print(student5)
