import json

file = open("friends_json.txt","r")
fileContents = json.load(file)
file.close()
name = {'make' : 'Ford', 'model' : 'Fiesta'}
fileContents["friends"].append(name)
with open("friends_json.txt","w") as data:
    json.dump(fileContents,data,sort_keys=True,indent=1)

# cars = [
#     {'make' : 'Ford', 'model' : 'Fiesta'},
#     {'make' : 'Ford', 'model' : 'Focus'},
# ]

# file = open("car_json.txt","w")

# json.dump(cars,file)
# file.close()

# cs = '[{"make": "Ford", "model": "Fiesta"}, {"make": "Ford", "model": "Focus"}]'

# pr = json.loads(cs)
# print(pr[0]['make'])
