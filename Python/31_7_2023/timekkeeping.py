import time

start = time.time()

ptr = [lambda limit: x**2 for x in range(5000000)]

end= time.time()
print(end-start)