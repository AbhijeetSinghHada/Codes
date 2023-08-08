import time
from threading import Thread


def ask_user():
    start = time.time()
    user_input = input('Enter your name : ')
    greet = f'Hello, {user_input}'
    print(greet)
    print(f'ask_user, {time.time()-start}')


def complex_cal():
    start = time.time()
    print("Starting Calculation...")
    [x**2 for x in range(20000000)]
    print(f'complex_cal, {time.time()-start}')


start = time.time()
ask_user()
complex_cal()
print(f'Single Threaded Total Time, {time.time()-start}')

thread1 = Thread(target=complex_cal)
thread2 = Thread(target=ask_user)
thread3 = Thread(target=complex_cal)

start = time.time()
thread2.start()
thread1.start()
thread3.start()

thread2.join()
thread1.join()
thread3.join()
print(f'Two Threaded Total Time, {time.time()-start}')
