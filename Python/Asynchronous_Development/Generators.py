def countdown(n):
    while n > 0:
        yield n
        n -= 1


for i in countdown(10):
    print(i)
# tasks = [countdown(10), countdown(5), countdown(20)]
# while tasks:
#     task = tasks[0]
#     tasks.remove(task)
#     try:
#         x = next(task)
#         print(x)
#         tasks.append(task)
#     except StopIteration:
#         print('Task Finished')
