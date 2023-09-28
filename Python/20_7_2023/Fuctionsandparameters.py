# def add(x,y=4):
#     return f"{x+y} : val of x = {x}, val of y = {y}"

# print(add(4,6))
# print(add(4,y=46))
# print(add(y=4,x=46))

# noow lambda function
def sub(x, y): return x-y
def add(x, y): return x+y


def mul(x, y): return x*y


operations = {
    "subtract": sub,
    "addition": add,
    "multiply": mul
}

operation_input = input()
x, y, a = map(int, input("Enter Value of x and y : ").split())
print(a)
print(type(a))
print(list(a))
print(operations[operation_input](x, y))
