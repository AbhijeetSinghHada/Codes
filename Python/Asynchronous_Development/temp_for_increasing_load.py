from threading import Thread


def fib(n):
    if n < 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)


def load_increase():
    while True:
        usn = int(input("Enter : "))
        fib(usn)


Thread(target=load_increase).start()
