import time
from concurrent.futures import ThreadPoolExecutor


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

start = time.time()
with ThreadPoolExecutor(max_workers=2) as pool:
    pool.submit(complex_cal)
    pool.submit(ask_user)
print(f'Two Threaded Total Time, {time.time()-start}')
