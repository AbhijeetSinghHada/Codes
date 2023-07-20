# SampleList = ["A","B","C","D","E"]

# copyList = SampleList


# copyList[0]= "Editied"

# print(SampleList,"   ",copyList)

# SampleList = copyList.copy()

# SampleList[0]= "Origional"

# print()
# print(SampleList,"   ",copyList)
# print()
# SampleList = copyList[:]
# copyList[0]= "Editied"
# print(SampleList,"   ",copyList)

import copy


data1 = 10
data2 = 20
data3 = 30

SampleList= [10,20,30]

print(SampleList)
print()
CopyList = (SampleList)
SampleList[0]= "Changed"
print(SampleList,"     ",CopyList)