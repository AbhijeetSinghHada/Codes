for x in range(2, 20):
    for y in range(2, x//2):
        if (x % y == 0):
            break
    print(f"{x}")

# Prime number code
for x in range(2, 20):
    for y in range(2, x//2):
        if (x % y == 0):
            break
    else:
        print(f"{x}")
