import json


class DeleteEmployee:
    def __init__(self, employee_name):
        self.name = employee_name
        self.delete_employee()

    def delete_employee(self):
        with open("data.json", "r") as file:
            data = json.load(file)

        for emp in data["employee"]:
            count = 0
            if emp["name"] == self.name:
                del data["employee"][count]
            count += 1

        with open("data.json", "w") as file:
            json.dump(data, file, indent=2)

        print(data)
