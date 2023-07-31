#Generator Expression:
import timeit

gen_exp = (i for i in range(1000000) if i % 2 == 0)

print(timeit.timeit(f"print(list[{gen_exp}]"))

#List Comprehension:

list_com = [i for i in range(100) if i % 2 == 0]

print(timeit.timeit('''print(list_com)''', number=1000000))