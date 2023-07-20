def over_age(data, getter):
    print(data,"  ",getter)
    return getter(data) >= 18
 
user = { 'username': 'rolf123', 'age': '35' }
 
print(over_age(user, lambda x: int(x['age'])))