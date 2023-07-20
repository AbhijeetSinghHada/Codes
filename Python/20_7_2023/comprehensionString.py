SampleNumbers = [1,2,3,4,5,6,7,8,9,10]

doubledNumbers = [number * 3 for number in SampleNumbers]

print(doubledNumbers)

TableOfThree = [f"Table of three {number*3}" for number in SampleNumbers]

TableOfThree = "\n".join([str(numbers) for numbers in TableOfThree])

print(TableOfThree)
 
 
#---------------------------------------x-----------------------------------
# using sets
football ={"Abhi","Pranu","Kittu","Modi"}

print([lowerCase.lower() for lowerCase in football ])

players = [
    {"Name":"Abhi",
     "Number":[1,8,3,13,21]},
    {"Name":"Kittu",
     "Number":[5,7,4,12,9]
     }
]
for x in players:
    for name in x["Name"]:
        print(name)
    