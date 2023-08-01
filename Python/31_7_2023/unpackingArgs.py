class User:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        
    # @classmethod
    # def from_dict(cls,data):
    #     return cls(data['username'], data['password'])
    
users = [
    {'username': 'abhi', 'password': '123'},
    {'username': 'kittu', 'password': '2233'}    
    ]
# userL = [User.from_dict(user) for user in users]
# print(userL[0].username)
# userM = map(User.from_dict,users)
# a = next(userM)
# print(a.username, a.password)
# a = next(userM)
# print(a.username, a.password)
user = [User(**us) for us in users]
print(user[0].username)
