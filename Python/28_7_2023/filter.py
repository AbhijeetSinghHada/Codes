# def start_with_r(friends):
#     return friends.startswith('R')   #Better to use lambda instead
friends = ['Raksha','Abhi','Raju','Ram','Kittu']

Starts_with_r= filter(lambda x: x.startswith("R"),friends)

another_func = (x.startswith('R') for x in friends)

test = [lambda friends: x.startswith('R') for x in friends]

print(another_func)
print(next(another_func))
print(list(another_func))
print(list(Starts_with_r))