from abc import ABC, abstractmethod


class A(ABC):

    @abstractmethod
    def test2(self):
        print('in test 2')


class B(A):
    def printss():
        print("Hello")


b = B()
b.test2()
