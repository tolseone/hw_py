# На вход программе на первой строке подаются коэффициенты многочлена, разделенные символом пробела и целое число
# x на второй строке. Напишите программу, которая вычисляет значение указанного многочлена при заданном значении x.
### Формат входных данных
# На вход программе на первой строке подаются коэффициенты многочлена (целые числа), разделенные символом пробела и целое число x на второй строке.
### Формат выходных данных
# Программа должна вывести одно число — значение указанного многочлена при заданном значении x.

# Решение задачи необходимо оформить в виде функции evaluate(coefficients, x), которая принимает список коэффициентов и значение аргумента. 
# Функция evaluate() должна быть реализована на основе встроенных функций map() и reduce().
import functools, operator
def evaluate(args: list, x: int):
    return functools.reduce(lambda z, t: z + t, list(map(lambda a, b: operator.mul(x ** b, a), args, list(range(len(args)))[::-1])), 0)


print(evaluate(list(map(int, input().split())), x = int(input())))
