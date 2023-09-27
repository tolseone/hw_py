class Clock:
    __DAY = 86400 # число секунд в одном дне

    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError("Секунды должны быть целым числом")
        self.seconds = seconds % self.__DAY

    def get_time(self):
        s = self.seconds % 60
        m = (self.seconds // 60) % 60
        h = (self.seconds // 3600) % 24
        return f"{self.__get_formatted(h)}:{self.__get_formatted(m)}:{self.__get_formatted(s)}"
    
    @classmethod
    def __get_formatted(cls, x):
        return str(x).rjust(2, "0")
    
    def __add__(self, other):
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError("Правый операнд должен быть int")
        
        sc = other
        if isinstance(sc, Clock):
            sc = other.seconds

        return Clock(self.seconds + sc)
    
    def __radd__(self, other): # метод, если запись типа c3 = 3213 + c3 (числовое значение слева!!!)
        return self + other
    
    def __iadd__(self, other):
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError("Правый операнд должен быть int или Clock")
        
        sc = other
        if isinstance(sc, Clock):
            sc = other.seconds
        
        self.seconds += sc
        return self

c1 = Clock(1000)
c2 = Clock(3000)
c4 = Clock(100000)
# c1.seconds = c1.seconds + 100     # без метода __add__
c1 = c1 + 100                       # == c1.__add__(100) - с использованием метода __add__
c3 = c1 + c2 + c4                   # Можем складывать больше 2 значений - с помощью __add__ (c1.__add__(c2) c3.__add__(c1))
c3 = 324 + c3                       # Метод __radd__, который перекидывает на метод __add__
c3 += 400                           # Метод __iadd__ для операций типа c3 += 100 
print(c3.get_time())