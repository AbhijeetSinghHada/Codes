#Generator Expression:
import timeit

print(timeit.timeit('''gen_exp = (i for i in range(100) if i % 2 == 0)''', number=1000000))
#List Comprehension:

print(timeit.timeit('''list_com = [i for i in range(100) if i % 2 == 0]''', number=1000000))
