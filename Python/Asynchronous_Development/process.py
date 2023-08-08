import time
from concurrent.futures import ProcessPoolExecutor
# from multiprocessing import Process


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


if __name__ == '__main__':
    start = time.time()
    # ask_user()
    complex_cal()
    complex_cal()
    print(f'Single Threaded Total Time, {time.time()-start}')

    # process1 = Process(target=complex_cal)
    # process2 = Process(target=complex_cal)
    # process1.start()
    # process2.start()
    start = time.time()
    with ProcessPoolExecutor(max_workers=2) as pool:
        pool.submit(complex_cal)
        pool.submit(complex_cal)
    # process1.join()
    # process2.join()

    print(f'Two Threaded Total Time, {time.time()-start}')
