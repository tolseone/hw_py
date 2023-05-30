# В списке хранятся числа, вывести список четных чисел и их квадраты

list_1 = [1, 2, 3, 5, 8, 15, 23, 38]
new_list = [(eto_chislo, eto_chislo ** 2) for eto_chislo in list_1 if eto_chislo % 2 == 0]
print(new_list)






















# def do_something(operation, arg):
#     print(operation(arg))

# do_something(lambda list:[(element, element ** 2) for element in list if element % 2 == 0], list_1)
