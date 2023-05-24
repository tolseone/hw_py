# В списке хранятся числа, вывести список четных чисел и их квадраты

list_1 = [1, 2, 3, 5, 8, 15, 23, 38]


def do_something(operation, arg):
    print(operation(arg))

do_something(lambda list:[(element, element ** 2) for element in list if element % 2 == 0], list_1)
