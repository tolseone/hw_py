# Подвиг 5. Объявите класс Animal (животное), объекты которого создаются командой:

# an = Animal(name, kind, old)
# где name - название животного (строка); kind - вид животного (строка); old - возраст (целое число). В каждом объекте этого класса должны создаваться соответствующие приватные атрибуты: __name, __kind, __old.

# В классе Animal должны быть объявлены объекты-свойства для изменения и считывания приватных атрибутов:

# name - для работы с приватным атрибутом __name;
# kind - для работы с приватным атрибутом __kind;
# old - для работы с приватным атрибутом __old.

# Создайте в программе список с именем animals, который содержит три объекта класса Animal со следующими данными:

# Васька; дворовый кот; 5
# Рекс; немецкая овчарка; 8
# Кеша; попугай; 3

# P.S. В программе нужно объявить только класс и создать список animals. На экран выводить ничего не нужно.

class Animal:
    def __init__(self, name, kind, old):
        self._verify_data(name, str)
        self.__name = name
        self._verify_data(kind, str)
        self.__kind = kind
        self._verify_data(old, int)
        self.__old = old

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, new_name):
        self._verify_data(new_name, str)
        self.__name = new_name

    @property
    def kind(self):
        return self.__kind
    
    @kind.setter
    def kind(self, new_kind):
        self._verify_data(new_kind, str)
        self.__kind = new_kind

    @property
    def old(self):
        return self.__old
    
    @old.setter
    def old(self, new_old):
        self._verify_data(new_old, int)
        self.__old = new_old

    def _verify_data(self, data, type_data):
        if not isinstance(data, type_data):
            raise TypeError(f"неверный тип данных, должно быть {type_data}")

info_animals = (("Васька", 'дворовый кот', 5),
        ('Рекс', 'немецкая овчарка', 8),
        ('Кеша', 'попугай', 3),)

animals = [Animal(*data) for data in info_animals]
print(animals[0].kind)