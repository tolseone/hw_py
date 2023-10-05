# Полиморфизм – это возможность работы с совершенно разными объектами (языка Python) единым образом.

# Абстрактные методы - методы, которые обязательно нужно переопределять в дочерних классах и которые не имеют своей собственной реализации
# В Python нет чисто абстрактных методов, мы лишь выполняем имитацию их поведения, заставляя программиста переопределять метод в дочерних классах,
# самостоятельно генерируя исключение raise NotImplementedError()

class Geom: # Абстрактный класс с абстрактным методом get_pr()
    def get_pr(self):
        raise NotImplementedError("В дочернем классе должен быть переопределен метод get_pr()")

class Rectangle(Geom):
    def __init__(self, w, h):
        self.w = w
        self.h = h
 
    def get_pr(self):
        return 2*(self.w+self.h)
 
 
class Square(Geom):
    def __init__(self, a):
        self.a = a
 
    def get_pr(self):
        return 4*self.a
    
class Triangle(Geom):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
 
    def get_pr(self):
        return self.a + self.b + self.c
    
# # объявлены геттеры get_rect_pr() и get_sq_pr() для получения периметра соответствующих фигур: прямоугольника и квадрата. 
# # Далее, мы можем создать экземпляры этих классов и вывести в консоль значения периметров
# r1 = Rectangle(1, 2)
# r2 = Rectangle(3, 4)
# print(r1.get_rect_pr(), r2.get_rect_pr())
# s1 = Square(10)
# s2 = Square(20)
# print(s1.get_sq_pr(), s2.get_sq_pr())
# # Все отлично, все работает. Но, теперь предположим, что все эти объекты помещаются в коллекцию:
# geom = [r1, r2, s1, s2]
# for g in geom:
#     print(g.get_rect_pr())
# # когда в цикле очередь дойдет до объекта s1, возникнет ошибка, 
# # т.к. в классе Square отсутствует метод get_rect_pr(). Конечно, зная, что в коллекции находятся объекты Rectangle и Square