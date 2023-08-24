class Vector:
    MIN_COORD = 0
    MAX_COORD = 10

    @classmethod                                  
    def validate(cls, arg):   # cls - отличие от обычных классов (ССЫЛКА НА КЛАСС Vector)
        return cls.MIN_COORD <= arg <= cls.MAX_COORD  # метод @classmethod работает исключительно только с атрибутами класса
                                                        #(не может обращаться к локальным атрибутам экземпляра класса)
        
    def __init__(self, x, y) -> None:
        self.x = self.y = 0
        if self.validate(x) and self.validate(y):     # можем вызывать внутри других методов для проверки соответствия
                                                          # Также, вместо Vector.validate(x) НУЖНО! использовать self.validate(x) - так как в self хранится информация о классе
            self.x = x   # присвоит значения локальных атрибутов x и y, если условие выполняется, иначе self.x = 0 и self.y = 0 
            self.y = y
        print(self.norm2(self.x, self.y)) # вызов статикметода внутри __init__()

    def get_coords(self):
        return self.x, self.y
    

    @staticmethod   # некая сервисная вспомогательная функция, которая помогает нам вычислять квадратичную норму вектора
    def norm2(x, y):
        return x*x + y*y
    
v = Vector(1, 2) # создание экземпляра класса Vector
res = v.get_coords() # вызов метода get_coords() ---> (1, 2) через экземпляр класса

res_analog = Vector.get_coords(v) # вызов метода get_coords() через класс Vector с экземпляром v, который явно указан в методе get_coords()

result = Vector.validate(5)   # метод класса мы можем спокойно вызывать через сам класс
print(result)

print(Vector.norm2(5, 6)) # вызов @staticmethod

### Методы класса предназначены для работы с атрибутами класса и переданными аргументами, а статические - только с переданными им аргументами

