# football =["Abhi","Pranu","Kittu","Modi"]
# SampleNumbers = [1,2,3,4,5,6,7,8,9,10]

# LenghtOfFootballerNames = [
#     length 
#     for length in SampleNumbers 
#     if length in [len(f) for f in football]
#     ]

# print(LenghtOfFootballerNames)

#-----------------------------------x-------------------------------------#

football ={"Abhi","Pranu","Kittu","Modi"}
SampleNumbers = {1,2,3,4,5,6,7,8,9,10}

LenghtOfFootballerNames = {
    length 
    for length in SampleNumbers 
    if length in {len(f) for f in football}
}

print(LenghtOfFootballerNames)
