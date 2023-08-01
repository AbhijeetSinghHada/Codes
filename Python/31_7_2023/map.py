friends = ['Raksha','Abhi','Raju','Ram','Kittu']

x = map(lambda x: x.lower(), friends)
print(list(x))

x = (x.lower() for x in friends)
print(x)
print(next(x))
print(next(x))
print('Hello')
print(next(x))
print(next(x))
print(next(x))
print(next(x))


# class User:
#     def __init__(self,username,password):
#         self.username = username
#         self.password = password
        
#     @classmethod
#     def from_dict(cls,data):
#         return cls(data['username'], data['password'])
    
# users = [
#     {'username': 'abhi', 'password': '123'},
#     {'username': 'kittu', 'password': '2233'}    
#     ]
# userL = [User.from_dict(user) for user in users]
# print(userL[0].username)
# userM = map(User.from_dict,users)
# a = next(userM)
# print(a.username, a.password)
# a = next(userM)
# print(a.username, a.password)
