from typing import List

class Employee:
    def __init__(self, name: str, age: int, salary: float, department: str):
        self.name = name
        self.age = age
        self.salary = salary
        self.department = department

class Company:
    def __init__(self, name: str, employees: List[Employee]):
        self.name = name
        self.employees = employees

    def get_department_employees(self, department: str) -> List[Employee]:
        return [employee for employee in self.employees if employee.department == department]

    def get_average_salary(self) -> float:
        return sum([employee.salary for employee in self.employees]) / len(self.employees)


employee1 = Employee(name="Abhi", age=21, salary=30000.0, department="Engineering")
employee2 = Employee(name="Aaryan", age=20, salary=60000.0, department="Engineering")
employee3 = Employee(name="Kittu", age=19, salary=70000.0, department="Sales")
employee4 = Employee(name="Raksha", age=24, salary=80000.0, department="Accounts")

company = Company(name="ABC Corp", employees=[employee1, employee2, employee3, employee4])

sales_employees = company.get_department_employees("Sales")
print("Sales Employees:")
for employee in sales_employees:
    print(f"{employee.name} ({employee.age}) - ${employee.salary}")

average_salary = company.get_average_salary()
print(f"\nAverage Salary: ${average_salary}")