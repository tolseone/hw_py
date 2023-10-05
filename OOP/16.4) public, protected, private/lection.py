# attr - public
# _attr - protected - служит для обращения внутри класса и во всех его дочерних классах
# __attr - private - служит для обращения только внутри класса

# Все приватные свойства и атрибуты формируются таким образом: в том классе, где они прописаны - тот и префикс и добавляется: _Geom__x1, _Rect__fill

class Geom:
    name = "Geom"

    def __init__(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

    def get_coords(self):
        return self.__x1, self.__y1
    
class Rect(Geom):
    def __init__(self, x1, y1, x2, y2, fill='red'):
        super().__init__(x1, y1, x2, y2)
        self.__fill = fill

r = Rect(1, 2, 10, 20)
print(r.get_coords()) # Можно, так как обращение к приватныым атрибутам происходит через метод внутри класса, где прописаны эти приватные атрибуты
