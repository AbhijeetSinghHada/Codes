fs = open("csvfile.txt", "r")
lines = fs.readlines()
fs.close()
lines = [line.strip().split(",") for line in lines]
for line in lines:
    name= line[0].title()
    age = line[1]
    degree = line[2].upper()
    college = line[3].upper()
    print(f"{name} is {age} years old, has a {degree} degree from {college}.")