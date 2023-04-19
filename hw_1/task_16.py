# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai (можно использовать псевдогенерацию). 
# Последняя строка содержит число X.

from random import *

def creating_array():
    N = int(input("Введите длину массива: "))
    list_1 = []
    for i in range(N):
        list_1.append(randint(3, 5))
    return list_1

def search_item():
    X = int(input("Введите число, которое нужно найти в массиве: "))
    list_2 = creating_array()
    count = 0
    for i in range(len(list_2)):
        if list_2[i] == X:
            count += 1
    return list_2

print(search_item())

