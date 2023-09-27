# Подвиг 10 (на повторение). Объявите класс PolyLine (полилиния) для представления линии из последовательности прямолинейных сегментов. Объекты этого класса должны создаваться командой:

# poly = PolyLine(start_coord, coord_2, coord_3, ..., coord_N)
# Здесь start_coord - координата начала полилинии (кортеж из двух чисел x, y); coord_2, coord_3, ... - последующие координаты точек на плоскости (представленные кортежами), соединенных прямыми линиями.

# Например:

# poly = PolyLine((1, 2), (3, 5), (0, 10), (-1, 8))


# В классе PolyLine должны быть объявлены следующие методы:

# add_coord(x, y) - добавление новой координаты (в конец);
# remove_coord(indx) - удаление координаты по индексу (порядковому номеру, начинается с нуля);
# get_coords() - получение списка координат (в виде списка из кортежей).

# P.S. На экран ничего выводить не нужно, только объявить класс.

class PolyLine:
    def __init__(self, *args):
        self.line = list(args)

    def add_coord(self, x, y):
        self.line.append((x, y))

    def remove_coord(self, indx):
        self.line.pop(indx)

    def get_coords(self):
        return self.line
    
p = PolyLine((1, 2), (3, 4), (5, 6))
p.add_coord(7, 8)
p.remove_coord(1)
print(p.get_coords())