import json
from Employee import Employee

class AddEmployee(Employee):
    def __init__(self, employee):
        self.name = employee.employee_name
        self.id = employee.employee_id
        self.email = employee.employee_email
        self.department = employee.employee_department

    def add_emp(self):
        emp = {
            "name": self.name,
            "id": self.id,
            "email": self.email,
            "department": self.department
        }
        with open("data.txt", "r") as my_file:
            data = json.load(my_file)

        data["employee"].append(emp)
        with open("data.txt", "w") as my_file:
            json.dump(data, my_file, sort_keys=True, indent=1)
