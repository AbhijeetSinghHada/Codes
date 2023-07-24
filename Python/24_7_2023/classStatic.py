from datetime import date
class Person:
    def __init__(self,name ,year) -> None:
        self.name = name
        self.year = year
    
    @classmethod
    def from_birth_year(cls, name , year):
        return cls(name, date.today().year-year)
    
    @staticmethod
    def isAdult(year):
        return year>=18
    
    def show_details(self):
        print(self.name," ", self.year)
    
p1= Person("Abhijeet", 18)
p2 = Person.from_birth_year("Abhi", 1999)

p1.show_details()
p2.show_details()

print(Person.isAdult(18))
