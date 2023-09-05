class Person:
    def __init__(self, name, old):
        self.__name = name
        self.__old = old

    def get_old(self):
        return self.__old
 
    def set_old(self, old):
        self.__old = old

    old = property(get_old, set_old)

p = Person("Tolya", 21)
p.set_old(22) # обычный способ изменения локальной переменной __old при помощи сеттера set_old
print(p.get_old()) # получение локальной переменной __old при помощи геттера get_old

p2 = Person("Nastya", 23)
p2.old = 25 # При помощи property вызов сеттера
print(p2.old) # При помощи property вызов геттера