class Point:
    color = "red"
    circle = 2

    def set_coords():
        print("вызов метода set_coords")

# Point.set_coords ### <function Point.set_coords at 0x..>
# Point.set_coords() ### вызов метода

# pt = Point.set_coords()
# pt.set_coords ### <bound fucni....>
# pt.set_coords() ### ошибка, так как должен поступать 1 аргумент self

class Point:
    color = "red"
    circle = 2

    def set_coords(self, x, y):
        self.x = x # локальное свойство
        self.y = y # локальное свойство

    def get_coords(self):
        return (self.x, self.y)

pt = Point()
pt.set_coords(1, 2)
print(pt.get_coords())
pt2 = Point()
pt2.set_coords(10, 20)
print(pt2.__dict__)
f = getattr(pt2, "get_coords")
print(f())
# Point.set_coords() ### будет ошибка, так как обращение к методу класса через класс.
# Point.set_coords(pt) ### Всё будет работать, так как указали объект класса Point в методе set_coords()
