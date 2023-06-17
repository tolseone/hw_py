# array_with_difference_azumits = []
# for i in range(len(array_with_azumits) - 1):
#     dif_azum = array_with_azumits[i + 1] - array_with_azumits[i]
#     # if dif_azum < 0:
#     #     dif_azum += 180
#     # if dif_azum < 0:
#     #     dif_azum += 180
#     array_with_difference_azumits.append(dif_azum)
# if array_with_azumits[0] == 0:
#     array_with_azumits[0] = 360
# dif_azum = array_with_azumits[0] - array_with_azumits[-1]
# if dif_azum < 0:
#     dif_azum += 180
# if dif_azum < 0:
#     dif_azum += 180
# array_with_difference_azumits.append(dif_azum) # матрица разности азимутов в градусах
# print(f"Матрица разности азимутов в градусах: {array_with_difference_azumits}")
# array_radians = [paramert * pi/180 for paramert in array_with_difference_azumits]
# print(f"Матрица разности азимутов в радианах: {array_radians}") # матрица разности азимутов в радианах
# print(array_with_azumits)
# print(array_with_difference_azumits)
# matrix_A = [
#       [a11, a12],
#       [a21, a22]]

# [
#     [sin(Ai)tan(hi) - sin(Aj)tan(hj), cos(Aj)tan(hj) - cos(Ai)tan(hi)] 11  12  A2 - A1   A2 - A1
#     [sin(Ai)tan(hi) - sin(Aj)tan(hj), cos(Aj)tan(hj) - cos(Ai)tan(hi)] 21  22  A3 - A2   A3 - A2
#     [sin(Ai)tan(hi) - sin(Aj)tan(hj), cos(Aj)tan(hj) - cos(Ai)tan(hi)] 31  32  A1 - A3   A1 - A3
# ]
# sin(), cos(), tan()