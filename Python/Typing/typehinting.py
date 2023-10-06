
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def __str__(self):
        return f'{self.name} is {self.age} years old.'
    
person1 = Person('John', 36)

# def func(person):
#     print(person.name)
#     print(person.age)

def func(person : Person):
    print(person.name)
    print(person.age)

func(person1)