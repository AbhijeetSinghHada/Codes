from threading import Thread
import time
import random
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',
                    filename='logs.txt'
                    )
logger = logging.getLogger('fuzzying')
counter = 0


def increment_counter():
    global counter
    logger.info(f"String Thread as Having Count {counter}")
    time.sleep(random.random())
    counter += 1
    time.sleep(random.random())
    print(f'New Counter Value : {counter}')
    time.sleep(random.random())
    print('-------------------------------------------------------------------------------------')


for x in range(10):
    t = Thread(target=increment_counter)
    time.sleep(random.random())
    t.start()
