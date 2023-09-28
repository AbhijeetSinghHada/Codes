# from collections import namedtuple

# Account = namedtuple('Account', ['name', 'balance'])
# acc = Account('checking', 1850.90)
# print(acc.name)
# print(acc)

# print(acc._asdict())

l = ["1", "2", "3"]


def func(lst):
    lst = [100]


func(l)
l = l + [10]
print(l)
