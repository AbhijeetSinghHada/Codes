class generateNumber:
    def __init__(self):
        self.number=0
        
    def __next__(self):
        if self.number<100:
            current = self.number
            self.number +=1
            return current
        else:
            raise StopIteration()
class numberiterate:
    def __iter__(self):
        return generateNumber()
    def __next__(self):
        return next(generateNumber())
my_gen = numberiterate()

# print(my_gen.__next__())
print(sum(numberiterate()))

for i in numberiterate():
    print(i)