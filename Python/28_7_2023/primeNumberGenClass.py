class PrimeGenerator:
    # You may modify the __init__() method if necessary, but you don't need to change its arguments
    def __init__(self, stop):
        self.stop = stop # stop defines the range (exclusive upper bound) in which we search for the primes
        self.number = 2
    def __next__(self):
        for n in range(self.number, self.stop):
            for x in range(2, int(n/2)+1):
                if n % x == 0:
                    break
            else:
                self.number=n+1
                return n
a = PrimeGenerator(100)

for i in range(10):
    print(next(a))