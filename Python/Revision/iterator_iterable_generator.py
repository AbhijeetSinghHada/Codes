
class Iterator:
    def __init__(self, sequence):
        self.sequence = sequence
        self.index = 0

    def __next__(self):
        if self.index > len(self.sequence):
            raise StopIteration
        temp = self.sequence[self.index]
        self.index += 1
        return temp


class Iterable:
    def __init__(self, sequence) -> None:
        self.sequence = sequence

    def __iter__(self):
        return Iterator(self.sequence)


lst = [1, 2, 3, 4, 5, 6]

lst = Iterable(lst)
lst = lst.__iter__()
print(lst)
for i in range(10):
    print(next(lst))
