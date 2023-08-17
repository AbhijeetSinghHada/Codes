def func(**kwargs):
    print(kwargs)


def nice(**kwargs):
    func(**kwargs)
    for key, value in kwargs.items():
        print(f'{key} => {value}')


def main():
    dic = {'a': 1, 'b': 2, 'c': 3}
    nice(**dic)


if __name__ == '__main__':
    main()
