class Clock:
    __DAY = 86400 # число секунд в одном дне

    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError("Секунды должны быть целым числом")
        self.seconds = seconds % self.__DAY

    @classmethod
    def __verify_data(cls, other):
        if not isinstance(other, (int, Clock)):
            raise TypeError("Значение должно быть типа int или Clock")
        
        return other if isinstance(other, int) else other.seconds

    def __eq__(self, other):  # Переопределение сравнение 2 объектов класса Clock
        sc = self.__verify_data(other)
        return self.seconds == sc
    
    def __lt__(self, other):
        sc = self.__verify_data(other)
        return self.seconds < sc
    
    def __gt__(self, other):
        sc = self.__verify_data(other)
        return self.seconds > sc
    
    def __le__(self, other):
        sc = self.__verify_data(other)
        return self.seconds <= sc
    
    def __ge__(self, other):
        sc = self.__verify_data(other)
        return self.seconds >= sc
    
c1 = Clock(100)
c2 = Clock(200)
print(c1 == 100) # __eq__ - для равенства ==
print(c1 != 100) # ==> not(c1 == 100) __ne__ - обращается к методу __eq__
print(c1 < c2)   # __lt__ - для неравенства типа > или <
print(c1 > c2)   # обращается к __lt__ и меняет операнды местами ==> c2 < c1