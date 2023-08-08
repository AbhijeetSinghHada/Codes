'''
When multiple threads try to access the same content at the same time this results in unexpected behaviour. 
Hence we need to implement the queuing mechenism to do the the task in ordered way as expected.
See Fuzzying.py
'''
import time
import random
import queue
from threading import Thread

counter = 0
job_queue = queue.Queue()  # things to be printed by
counter_queue = queue.Queue()  # amounts by which to increase counter


def increment_mananger():
    global counter
    while True:
        # this waits until an item is availabe and then locks the queue
        counter += counter_queue.get()
        time.sleep(random.random())

        job_queue.put(
            (f'New counter Value is {counter}', '------------------'))
        counter_queue.task_done()


Thread(target=increment_mananger, daemon=True).start()


def printer_manager():
    while True:
        time.sleep(random.random())
        for line in job_queue.get():
            print(line)

        job_queue.task_done()


Thread(target=printer_manager, daemon=True).start()


def increment_counter():
    counter_queue.put(1)


worker_thread = [Thread(target=increment_counter) for thread in range(10)]
for thread in worker_thread:
    thread.start()

for thread in worker_thread:
    thread.join()
    print(thread.is_alive())

counter_queue.join()
job_queue.join()
