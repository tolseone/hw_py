# Задача: C клавиатуры вводится некий набор чисел, в качестве разделителя
# используется пробел. Этот набор чисел будет считан в качестве строки. Как
# превратить list строк в list чисел?

# list_1 = input().split()
# list_1 = list(map(int, list_1))
# list_1 = list(filter(lambda i: i % 2 == 0, list_1))
# print(list_1)

res = list(zip([1, 2, 3], ["Настя", "Толя"], [1.4, 1.3, 1.6]))
print(res)
family = ["папа", "мама", "брат", "я"]
print(list(enumerate(family)))
















# res = list(map(int, input().split()))
# print(res)