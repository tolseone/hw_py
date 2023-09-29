class Geom: # Базовый класс
    name = "GEOM"

    def set_coords(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
    
class Line(Geom): # Дочерний класс
    name = "Line"
    
    def draw(self):
        print("Линия")

class Rect(Geom): # Дочерний класс
    def draw(self):
        print("Квадрат")

L = Line()
R = Rect()
L.set_coords(1, 2, 3, 4) # При вызове метода set_coords объектом класса Line сначала:
                                # 1) Будет поиск метода set_coords внутри класса Line
                                # 2) Если не найдётся, то поиск будет произведён в родительском классе Geom
                                # 3) При этом, ВАЖНО, ссылка self будет указывать на класс Line (внутри метода set_coords)

R.set_coords(1, 2, 3, 4)        # Всё тоже самое, но ссылка self будет указывать на класс Rect (параметр self базового класса, может ссылаться не только
                                # на объекты базового класса, но также и на объекты дочерних классов)

print(L.__dict__)
print(R.__dict__)