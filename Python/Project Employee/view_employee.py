import json

class View:
    def fetch_data(self):
        with open("data.json", "r") as my_file:
            self.contents = json.load(my_file)
            return self.contents
            
    def view_data(self):
        print("Employee Database : ")
        for i,emp in enumerate(self.contents['employee'],start=1):
            print(f"\nEmployee {i} Data : \n")
            print(f"Name : {emp['name']}")
            print(f"ID : {emp['id']}")
            print(f"Department : {emp['department']}")
            print(f"Email : {emp['email']}")
 