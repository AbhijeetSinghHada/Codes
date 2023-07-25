# Please read the instructions carefully and write your script here:
# You need to:
# - read data from csv_file.txt
# - process data and convert them into a single JSON object
# - store the JSON object into json_file.txt
# Your code starts here:
import json
data = open("csv_file.txt","r")
contents = data.readlines()
data.close()

contents = [temp.strip().split(",") for temp in contents]
temp = [{"club" : temp[0],"country" : temp[2],"city" : temp[1]} for temp in contents]

with open('json_file.txt','w')as data:
    json.dump(temp,data)