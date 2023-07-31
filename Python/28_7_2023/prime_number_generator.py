def prime_generator(bound):
    prime=2
    for i in range(2,bound):
        for j in range(2,i):
            if(i%j==0):
                break
        else:
            yield i
g = prime_generator(100)

print(list(g))

        
