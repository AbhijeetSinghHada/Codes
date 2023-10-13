from dataclasses import dataclass, field, asdict, astuple


@dataclass(order=True)
class Student:
    index: int = field(init=False, repr=False)
    name: str = field(compare=False)
    age: int
    grade: int
    marks: float

    def __post_init__(self):
        self.index = self.age


student1 = Student("Abhi", 19, 12, 90.0)
student2 = Student("Kittu", 14, 8, 95.0)
student3 = Student("Raksha", 21, 12, 97.0)
student4 = Student("Happy", 19, 8, 91.0)
student5 = Student("Abhi2", 19, 12, 90.0)

print(student1 == student5)
