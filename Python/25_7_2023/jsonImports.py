import json

# file = open("friends_json.txt","r")
# fileContents = json.load(file)
# file.close()

# print(fileContents["friends"][0]["name"])

# cars = [
    # {'make' : 'Ford', 'model' : 'Fiesta'},
    # {'make' : 'Ford', 'model' : 'Focus'},
# ]
# file = open("car_json.txt","w")

# json.dump(cars,file)
# file.close()

cs = '[{"make": "Ford", "model": "Fiesta"}, {"make": "Ford", "model": "Focus"}]'

pr = json.loads(cs)
print(pr[0]['make'])
