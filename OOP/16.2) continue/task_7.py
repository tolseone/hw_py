# Подвиг 7. С помощью наследования можно как бы "наполнять" дочерние классы нужными качествами (свойствами). Как пример, объявите в программе класс с именем:

# Singleton

# который бы позволял создавать только один экземпляр (все последующие экземпляры должны ссылаться на первый). Как это делать, вы должны уже знать из этого курса.

# Затем, объявите еще один класс с именем:

# Game

# который бы наследовался от класса Singleton. Объекты класса Game должны создаваться командой:

# game = Game(name)
# где name - название игры (строка). В каждом объекте класса Game должен создаваться атрибут name с соответствующим содержимым.

# Убедитесь, что атрибут name принимает значение первого созданного объекта (если это не так, то поправьте инициализатор дочернего класса, чтобы это условие выполнялось).

# P.S. В программе нужно объявить только классы. Выводить на экран ничего не нужно.

class Singleton:
    __instanse = None
    _instance_base = None
    
    def __new__(cls, *args, **kwargs):
        if cls == Singleton: # если создаем экземпляр класа Singleton
            if cls._instance_base is None:
                cls._instance_base = object.__new__(cls)
            return cls._instance_base
        
        if cls.__instanse is None:   # если экземпляров класса не существует, то __instanse примет значение нового экзепляра класса Singleton
            cls.__instanse = object.__new__(cls)  
        return cls.__instanse # возвращаем значение __instanse

class Game(Singleton):
    def __init__(self, name):
        if 'name' not in self.__dict__: 
            self.name = name

s = Singleton()
g = Game("tolse")
g1 = Game("qwerty")
print(g.__dict__)
