# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

def create_arr():
    list = [int(input(f"Введите {i + 1} элемент: ")) for i in range(int(input("Введите длину массива: ")))]
    return list

# def creating_array(): ### Можно использовать и такую функцию
#     N = int(input("Введите длину массива: "))
#     list_1 = []
#     for i in range(N):
#         list_1.append(int(input("Введите элемент: ")))
#     return list_1

list_1, list_2 = create_arr(), create_arr() ### этот способ более компактен, но можно сделать как ниже
print("Первый набор чисел: ", list_1)
print("Второй набор чисел: ", list_2)
# list_1 = create_arr()
# print("Первый набор чисел: ", list_1)
# list_2 = create_arr()
# print("Первый набор чисел: ", list_2)
array_1, array_2 = set(list_1), set(list_2) ### Сортируем списки командой sorted(), приводим списки к множествами комадной set()
res = array_1.union(array_2)
print(f"Набор чисел, встречающихся в 2-ух введёных списках: {sorted(res)}")