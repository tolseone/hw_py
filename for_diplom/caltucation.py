from math import *
import numpy as np

def print_matrix(matrix):
    for row in matrix:
        for elems in row:
            print(str(elems).ljust(20), end=' ')
        print()

def menu():
    print(
        '1 - Взятие всех азимутов по порядку\n'
        '2 - Взятие азимутов попарно\n'
        '3 - Выход\n'
    )
     
def error():
    print("Ошибка, введённой команды не существует.")

h = int(input("Введите значение высоты в градусах: "))*pi/180 # в радианах
print(h)
m = 12 # минуты дуги
array_with_azumits = [int(input(f"Введите значение азимута на {i + 1} светило: ")) for i in range(int(input("Введите количество светил: ")))]
array_radians_1 =[radians(elem) for elem in array_with_azumits]
# print(f'Азимуты в радианах: {array_radians_1}')
while True:
    menu()
    user_answer = input("Введите команду: ")
    if user_answer == '1':
        matrix_A = [[sin(array_radians_1[i]) * tan(h) - sin(array_radians_1[i + 1]) * tan(h), cos(array_radians_1[i + 1]) * tan(h) - cos(array_radians_1[i]) * tan(h)] for i in range(len(array_radians_1) - 1)]
        matrix_A.append([sin(array_radians_1[-1]) * tan(h) - sin(array_radians_1[0]) * tan(h), cos(array_radians_1[0]) * tan(h) - cos(array_radians_1[-1]) * tan(h)])
        print("Матрица А:")
        print_matrix(matrix_A) # готовая матрица А
        A_transpose = np.transpose(matrix_A) # транспонированная матрица А
        prod_A = (np.dot(A_transpose, matrix_A)) # произведение матрицы А на матрицу Атранспонированную
        inversed_matrix = np.linalg.inv(prod_A) # обратная матрица
        print("Обратная матрица: ")
        print_matrix(inversed_matrix)
        Tr = sum([inversed_matrix[i][i] for i in range(len(inversed_matrix))])
        M = sqrt(Tr) * m # радиальная СКП
        print(f"След ковариационной матрицы = {Tr}\nРадиальная СКП = {M}")
    elif user_answer == "2":
        if len(array_radians_1) % 2 == 0:
            matrix_A_01 = [[sin(array_radians_1[i - 1]) * tan(h) - sin(array_radians_1[i]) * tan(h), cos(array_radians_1[i]) * tan(h) - cos(array_radians_1[i - 1]) * tan(h)] for i in range(1, len(array_radians_1), 2)]
            A_01_transpose = np.transpose(matrix_A_01)
            prod_A_01 = (np.dot(A_01_transpose, matrix_A_01))
            inversed_matrix_01 = np.linalg.inv(prod_A_01)
            print("Обратная матрица: ")
            print_matrix(inversed_matrix_01)
            Tr = sum([inversed_matrix_01[i][i] for i in range(len(inversed_matrix_01))])
            print(f"След для пар азимутов = {Tr}")
            M = sqrt(Tr) * m
            print(f"Радиальная СКП для пар азимутов = {M}")
        else:
            print("Количество введёных светил нечётно! Измените данные")
    elif user_answer == "3":
        print("Конец работы")
        break
    else:
        error()




# res = np.dot(m ** 2, inversed_matrix) # ковариационная матрица
# print("Ковариационная матрица: ")
# print_matrix()
# Tr = sum([res[i][i] for i in range(len(res))]) # след ковариационной матрицы 