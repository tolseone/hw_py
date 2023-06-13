from math import *
import numpy as np

def print_matrix(matrix):
    for row in matrix:
        for elems in row:
            print(str(elems).ljust(20), end=' ')
        print()
# A_1 = 0 # в градусах   0
# A_2 = 120 # в градусах 2*pi/3
# A_3 = 240 # в градусах 4*pi/3
h = int(input("Введите значение высоты в градусах: "))*pi/180 # в радианах
m = 0.2  # в градусах
m *= pi/180 # в радианах

# t_A_1 = A_2 - A_1
# t_A_2 = A_3 - A_2
# t_A_3 = A_1 - A_3

array_with_azumits = [int(input(f"Введите значение азимута на {i + 1} светило: ")) for i in range(int(input("Введите количество светил: ")))]
# print(array_with_azumits)
array_with_difference_azumits = []
for i in range(len(array_with_azumits) - 1):
    dif_azum = array_with_azumits[i + 1] - array_with_azumits[i]
    if dif_azum < 0:
        dif_azum += 360
    array_with_difference_azumits.append(dif_azum)
dif_azum = array_with_azumits[0] - array_with_azumits[-1]
if dif_azum < 0:
    dif_azum += 360
array_with_difference_azumits.append(dif_azum) # матрица разности азимутов в градусах
array_radians = [paramert * pi/180 for paramert in array_with_difference_azumits]
print(f"Матрица разности азимутов: {array_radians}") # матрица разности азимутов в радианах
# print(array_with_azumits)
# print(array_with_difference_azumits)
# matrix_A = [
#       [a11, a12],
#       [a21, a22]]

# [
#     [sin(Ai)tan(hi) - sin(Aj)tan(hj), cos(Aj)tan(hj) - cos(Ai)tan(hi)] 11  12
#     [sin(Ai)tan(hi) - sin(Aj)tan(hj), cos(Aj)tan(hj) - cos(Ai)tan(hi)] 21  22
#     [sin(Ai)tan(hi) - sin(Aj)tan(hj), cos(Aj)tan(hj) - cos(Ai)tan(hi)] 31  32
# ]
# sin(), cos(), tan()
matrix_A_1 = [sin(array_with_difference_azumits[i]) * tan(h) - sin(array_with_difference_azumits[0]) * tan(h) for i in range(len(array_radians))]
# print(matrix_A_1)
matrix_A = [[matrix_A_1[i], cos(array_with_difference_azumits[1])*tan(h) - cos(array_with_difference_azumits[i])*tan(h)] for i in range(len(matrix_A_1))]
print("Матрица А:")
print_matrix(matrix_A) # готовая матрица А
A_transpose = np.transpose(matrix_A) # транспонированная матрица А
prod_A = (np.dot(A_transpose, matrix_A)) # произведение матрицы А на матрицу Атранспонированную
inversed_matrix = np.linalg.inv(prod_A) # обратная матрица
print("Обратная матрица: ")
print_matrix(inversed_matrix)
res = np.dot(m ** 2, inversed_matrix) # ковариационная матрица
print("Ковариационная матрица: ")
print_matrix(res)
Tr = sum([res[i][i] for i in range(len(res))]) # след ковариационной матрицы 
M = sqrt(Tr) # радиальная СКП
print(f"След ковариационной матрицы = {Tr}\nРадиальная СКП = {M}")
# list_1 = [sin(array_with_difference_azumits[1]) * tan(h) - sin(array_with_difference_azumits[0]) * tan(h)]
# print(list_1)
# print(sin(array_with_difference_azumits[1]))
# print(sin(array_with_difference_azumits[0]))





