# lst = [["Abhi",22],["weff",23],["Sam",6]]

# print(lst)
# #lst[0].clear() #clears all the elements
# #lst[0].remove("Abhi")
# lst.remove(["Abhi"])
# print(lst)

#-----------------------------------------x------------------------------------------------

# football ={"Abhi","Pranu","Kittu","Modi"}
# TableTennis = {"Kittu", "Pranu","Nehru"}

# difference = football.difference(TableTennis)
# print(difference)# in football but not in TableTennis

# symdiff = football.symmetric_difference(TableTennis)
# print(symdiff) # not common in both

# same = football.union(TableTennis)
# print(same) #all elements 
# football.add
# inter = football.intersection(TableTennis)

# print(inter) 

#-----------------------------------------x---------------------------------------------------------

# dictionary = {"Abhi":21, "Chinki": 23, "Tunnu": 19}
# print(dictionary)
# dictionary["Happy"] = 46

# print(dictionary)
# print(dictionary.fromkeys(dictionary.keys()))
# ls = dictionary.values()

# dictionary = (
#     {"name": "Abhi", "age" : 32},
#     {"name": "Tuna", "age" : 22},
#     {"name": "Katy", "age" : 14},
    
# )
# i=0
# for i in range(len(dictionary)):
#     print(dictionary[i]["name"])

#--------------------------------------------x-------------------------------
# # Programming Assignment 

# lottery_numbers = {13, 21, 22, 5, 8}


# """
# A player looks like this:

# {
#     'name': 'PLAYER_NAME',
#     'numbers': {1, 2, 3, 4, 5}
# }

# Define a list with two players (you can come up with their names and numbers).
# """

# players = [
#     {"Name":"Abhi",
#      "Number":{1,8,3,13,21}},
#     {"Name":"Kittu",
#      "Number":{5,7,4,12,9}
#      }
# ]

# """
# For each of the two players, print out a string like this: "Player PLAYER_NAME got 3 numbers right.".
# Of course, replace PLAYER_NAME by their name, and the 3 by the amount of numbers they matched with lottery_numbers.
# You'll have to access each player's name and numbers, and calculate the intersection of their numbers with lottery_numbers.
# Then construct a string and print it out.

# Remember: the string must contain the player's name and the amount of numbers they got right!
# """
# print(f'Player {players[0]["Name"]} got {len(players[0]["Number"].intersection(lottery_numbers))} numbers right.')
# print(f'Player {players[1]["Name"]} got {len(players[1]["Number"].intersection(lottery_numbers))} numbers right.')

#-------------------------------------x--------------------------------------------------

players = [
    {"Name":"Abhi",
     "Number":[1,8,3,13,21]},
    {"Name":"Kittu",
     "Number":[5,7,4,12,9]
     }
]

commaSep = ", ".join(str(r) for r in players[0]["Number"])
print(commaSep)
print(f'{players[0]["Name"]} has {commaSep} numbers in his lottery.')

eg = set()
eg.add("gg")
