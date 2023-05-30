from math import *
# a = 15
# b = "хуй"
# c = 1.2
# def do_something():
#     return 0

# print(type(a), type(b), type(c), type(do_something))

# def one(a):
#     return sqrt(a)

def second(a):
    return int(pow(a, 2))

def result(operation_function, x, y):
    print(int(operation_function(x, y)))

result(lambda x, y: sqrt(x + y), 4, 5)

def do_1(x, y, z):
    return (x + y) // z

ya_umeu_tak = lambda x, y, z: ( x + y) // z
print(ya_umeu_tak(1, 2, 3))
print(do_1(1,2,3))
print(type(ya_umeu_tak
))
def do_2(x, y, z):
    return (pow(x, 10) + sqrt(y)) % z

do_2 = lambda x, y, z: (pow(x, 10) + sqrt(y)) % z



