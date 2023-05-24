# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и
# столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,
# которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте,
# почему не с нуля). Примечание: бинарной операцией называется любая операция, у которой
# ровно два аргумента, как, например, у операции умножения.
# Ввод: Вывод:
# print_operation_table(lambda x, y: x * y) 
#  1 2 3 4 5 6
#  2 4 6 8 10 12
#  3 6 9 12 15 18
#  4 8 12 16 20 24
#  5 10 15 20 25 30
#  6 12 18 24 30 36 

def print_operation_table(f, num_rows, num_columns):
    return (f(num_rows, num_columns))

n_rows, n_columns = int(input("Введите количество строк: ")), int(input("Введите количество столбцов: "))
res = print_operation_table(lambda rows, columns: [x * y for x in range(1, rows + 1) for y in range(1, columns + 1)], n_rows, n_columns)
for i in range(1, len(res) + 1):
    print(res[i - 1], end=' ')
    if i % (n_columns) == 0:
        print()
