temp = (1, 2, 3, 4, 5)


def sun(*arr):
    return sum(arr)


print(sum(temp))


def pretty_print(**kwargs):
    for k, v in kwargs.items():
        print(f'{k} maps to {v}')


pretty_print(name='Pannu', age=23, city='Delhi')
pretty_print(**{'name': 'bade PAPA', 'Age': '26'})
