fs = open("csvfile.txt", "w")
lines = fs.readlines()
fs.writelines
fs.close()
lines = [line.strip().split(",") for line in lines]
for line in lines:
    name= line[0].title()
    age = line[1]
    degree = line[2].upper()
    college = line[3].upper()
    print(f"{name} is {age} years old, has a {degree} degree from {college}.")