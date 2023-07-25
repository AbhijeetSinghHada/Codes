list_address = input("Enter the name of the file : ")
fileRead = open(list_address,"r")
user_list = fileRead.readlines()
fileRead.close()

user_list = [names.strip("\n") for names in user_list]

fileRead = open('friends.txt',"r")
friend_list = fileRead.readlines()
fileRead.close()

friend_list = [names.strip() for names in friend_list]

nearby_friends = [] 
for temp_friend in user_list:
    if temp_friend in friend_list:
        nearby_friends.append(temp_friend)

file_write = open('nearby_friends.txt',"w")
for temp in nearby_friends:
    file_write.write(f"{temp}\n")
file_write.close()

fileRead = open('nearby_friends.txt',"r")
nearby_friend_list = fileRead.readlines()
print("Your Closest Friends are : ")
print(nearby_friend_list)
fileRead.close()