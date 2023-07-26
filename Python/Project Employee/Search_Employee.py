import json


def search_emp(name):
    with open("data.json", "r") as my_file:
        data = json.load(my_file)
    for index,employee in enumerate(data["employee"]):
        if employee["name"] == name:
            department = employee["department"]
            print(f"{name.title()} is an employee of the organization of {department} department.")
            return index
    else:
        print(f"{name.title()} is not an employee of the organization.")
        return -1
