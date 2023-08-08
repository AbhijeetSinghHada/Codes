from threading import Thread
import time
n = 0


def monitor_req():
    global n
    while True:
        time.sleep(1)
        print(f"{n} -req/sec")
        n = 0


Thread(target=monitor_req).start()

while True:
    for x in range(100):
        x += 1
    n += 1
