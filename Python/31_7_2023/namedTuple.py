from collections import namedtuple

Account = namedtuple('Account',['name' ,'balance'])
acc = Account('checking',1850.90)
print(acc.name)
print(acc)

print(acc._asdict())``