import json
class Employee:
    def __init__(self, employee_id, employee_name, employee_email, employee_department):
        self.id = employee_id
        self.name = employee_name
        self.email = employee_email
        self.department = employee_department
        
    def add_emp(self):
        emp = {
            "name": self.name,
            "id": self.id,
            "email": self.email,
            "department": self.department
        }
        with open("data.json", "r") as my_file:
            data = json.load(my_file)

        data["employee"].append(emp)
        with open("data.json", "w") as my_file:
            json.dump(data, my_file, indent=1)