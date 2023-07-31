def hundred_numbers():
    i=0
    lst = []
    while i<100:
        lst.append(i)
        i+=1
    return lst 
# print (hundred_numbers())
def hundred_numbers_generator():
    i=0
    while i<100:
        yield i
        i+=1
g = hundred_numbers_generator()


print (hundred_numbers_generator().__class__)
print(id(hundred_numbers_generator()))
print (g.__class__)
print(id(g))
print (next(g))
print(id(g))
print (next(g))
print(id(g))
print(list(g))

        