# Объявите класс Point для представления точек на плоскости. Создавать объекты этого класса предполагается командой:
# pt = Point(x, y)
# Здесь x, y - числовые координаты точки на плоскости (числа), то есть, в каждом объекте этого класса создаются локальные свойства x, y, 
# которые хранят конкретные координаты точки.

# Необходимо в классе Point реализовать метод clone(self), который бы создавал новый объект класса Point как копию текущего объекта 
# с локальными атрибутами x, y и соответствующими значениями.

# Создайте в программе объект pt класса Point и еще один объект pt_clone через вызов метода clone.
# P.S. В программе на экран ничего выводить не нужно.

class Point:
    # __object = None

    # def __new__(cls, *args, **kwargs):
    #     cls.__object = super().__new__(cls)
    #     return cls.__object
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def clone(self):
        return Point(self.x, self.y)
    

pt = Point(1, 2)
pt_clone = pt.clone()
print(pt.__dict__, pt_clone.__dict__, sep='\n')
print(id(pt), id(pt_clone))
