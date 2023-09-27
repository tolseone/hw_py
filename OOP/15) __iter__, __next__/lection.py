# __iter__(self) – получение итератора для перебора объекта;
# __next__(self) – переход к следующему значению и его считывание.
# Итератор - это некий объект, у которого есть магический метод __next__ и вызывает этот магический метод __next__ функция next
class FRange:
    def __init__(self, start=0.0, stop=0.0, step=1.0):
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        self.value = self.start - self.step
        return self
    
    def __next__(self):
        if self.value + self.step < self.stop:
            self.value += self.step
            return self.value
        else:
            raise StopIteration

fr = FRange(0, 2, 0.5)

# print(next(fr)) # функция next неявно внутри себя вызывает метод __next__, а сам объект fr - выступает в роли итератора
# print(next(fr))
# print(next(fr))
# print(next(fr))

# it = iter(fr) 
for x in fr:  # неявно вызваны функции iter и next
    print(x)


class FRange2D:
    def __init__(self, start=0.0, stop=0.0, step=1.0, rows=5):
        self.rows = rows
        self.fr = FRange(start, stop, step)

    def __iter__(self):
        self.value = 0
        return self
    
    def __next__(self):
        if self.value < self.rows:
            self.value += 1
            return iter(self.fr)
        else:
            raise StopIteration

fr = FRange2D(0, 2, 0.5, 4)
for row in fr:
    for x in row:
        print(x, end=' ')
    print()


