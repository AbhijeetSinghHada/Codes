from collections import ChainMap


class Car:
    def __init__(self):
        self.cars = []
    def __len__(self):
        return len(self.cars)
    def __getitem__(self,index):
        return self.cars[index]
    def __str__(self):
        return (f"Hello, Bro {self.cars}")


carName = Car()
carName.cars.append("Ford")
carName.cars.append("Nano")


print((carName))

for car in carName:
    print(car)