list1 = ['A','B','C','D','E']

for counter,element in enumerate(list1):
    print(counter," : " ,element)
    
list2 = list(enumerate(list1,start=1))

print(list2)