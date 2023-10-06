from threading import Thread, Event


def task(event: Event, id: int):
    print(f"Starting task {id}")

    event.wait()

    print(f"Completed task {id}")


event1 = Event()
event2 = Event()

t1 = Thread(target=task, args=(event1, 1))
t2 = Thread(target=task, args=(event2, 2))

t1.start()
t2.start()

# this sets the event flag to true therfore the t1 thread is able to comlete its processing.
event1.set()

print("Execution of main is complete")

# if this is not set then program will never end and you will need to terminate the terminal.
event2.set()

# One event can be used in multiple processes simultaneously, acts just like mutex Locks
# from threading import Lock
