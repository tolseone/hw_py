class FibonacciGen:
    def __init__(self):
        self.prev = 0
        self.cur = 1

    def __next__(self):
        result = self.prev
        self.prev, self.cur = self.cur, self.prev + self.cur
        return result
    
    def __iter__(self):
        return self
    
def fibonacci():
    prev, cur = 0, 1
    while True:
        yield prev # Любая функция в Python, в теле которой встречается ключевое слово yield, называется генераторной функцией — при вызове она возвращает объект-генератор.
                # Объект-генератор реализует интерфейс итератора, соответственно с этим объектом можно работать, как с любым другим итерируемым объектом.
        prev, cur = cur, prev + cur

for num in fibonacci():
    print(num)

    if num > 100:
        break


# Рассмотрим работу yield:

def gen_fun():
    print('block 1')
    yield 1
    print('block 2')
    yield 2
    print('end')

for i in gen_fun():
    print(i)

# при вызове функции gen_fun создается объект-генератор
# for вызывает iter() с этим объектом и получает итератор этого генератора
# в цикле вызывает функция next() с этим итератором пока не будет получено исключение StopIteration
# при каждом вызове next выполнение в функции начинается с того места где было завершено в последний раз и продолжается до следующего yield

# Происходит приблизительно следующее. Генераторная функция разбивается на части:

# def gen_fun_1():
#     print('block 1')
#     return 1


# def gen_fun_2():
#     print('block 2')
#     return 2


# def gen_fun_3():
#     print('end')


# def gen_fun_end():
#     raise StopIteration

# Создается стейт-машина в которой при каждом вызове __next__ меняется состояния и в зависимости от него вызывается тот или иной кусок кода. 
# Если в функции yield в цикле, то соответственно состояние стейт-машины зацикливается пока не будет выполнено условие.

# СВОЙ ВАРИАНТ range

def cool_range(start, stop, step=1.0):
    x = start
    while x < stop:
        yield x
        x += step

for n in cool_range(1, 10, 1.5):
    print(n, end=' ')

def foo(*lst):
    for value in lst:
        yield from value
