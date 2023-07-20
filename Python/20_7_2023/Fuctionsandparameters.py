# def add(x,y=4):
#     return f"{x+y} : val of x = {x}, val of y = {y}"

# print(add(4,6))
# print(add(4,y=46))
# print(add(y=4,x=46))

#noow lambda function
sub = lambda x,y:x-y
add = lambda x,y: x+y
mul = lambda x,y:x*y

operations = {
    "subtract" : sub,
    "addition" : add,
    "multiply" : mul
}

operation_input = input()
x,y = map(int,input("Enter Value of x and y : ").split())
print(operations[operation_input](x,y))
