i=1
def greet():
    global i
    i+=1
    yield f"Hello, Boy{i}"


print(next(greet()))
print(i)

print(next(greet()))
print(i)