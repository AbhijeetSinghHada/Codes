import time
from threading import Thread


def ask_user():
    start = time.time()
    time.sleep(2)
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
# thread3 = Thread(target=complex_cal)

start = time.time()
thread1.start()
thread2.start()
# thread3.start()

# thread1.join() # if we do not join the thread1 then main thread only waits for thread one to complete not thread two
# but in background all are running simutaneously so thread1 completed then main completes its
# work till printing time of two threaded after that thread 1 output is printed
thread2.join()
# thread3.join()
print(f'Two Threaded Total Time, {time.time()-start}')
