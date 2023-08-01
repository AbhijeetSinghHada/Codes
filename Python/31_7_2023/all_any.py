friends = ['Raksha','Abhi','Raju','Ram','Kittu']

if any(friend.startswith('R') for friend in friends):
    print("My Friend has a R")

friends = ['Raksha','Rbhi','Raju','Ram','Rittu']
if all(friend.startswith('R') for friend in friends):
    print("My All Friends have a R")