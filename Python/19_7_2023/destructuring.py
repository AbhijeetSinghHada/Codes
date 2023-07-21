players = [
    {"Name":"Abhi",
     "Number":[1,8,3,13,21]},
    {"Name":"Kittu",
     "Number":[5,7,4,12,9]
     }
]
#i=int(0)
#for i in range(len(players)):
#    name,number = players[i].values()
#    print(name)
#    print(number)
#    i+=1
    
for f in players:
    name, number = f.items()
    print(name)
    print(number)
    