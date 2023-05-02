# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

def create_arr():
    list = [int(input(f"Введите {i + 1} элемент: ")) for i in range(int(input("Введите длину массива: ")))]
    return list

list_start = create_arr()
print(*list_start)
minimum = int(input("Введите нижнее значение диапазона: "))
maximum = int(input("Введите верхнее значение диапазона: "))

list_with_indexes = []
for i in range(len(list_start)):
    if minimum <= list_start[i] <= maximum:
        list_with_indexes.append(i)
print(f"индексы начального массива, элементы которых лежат между {minimum} и {maximum} : {list_with_indexes}")
