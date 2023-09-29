# НАСЛЕДОВАНИЕ КЛАССОВ ОТ КЛАССА OBJECT
class Geom(object): # явно прописанное наследование
    pass

class Line(Geom):
    pass

# g = Geom()
# l = Line()
# print(l.__class__)
# print(g) # Благодаря определению маг. метода __str__ в базовом классе object
# print(issubclass(Geom, Line))

class Vector(list):
    def __str__(self):
        return " ".join(map(str, self))
    
v = Vector([1, 2, 3])
print(str(v))