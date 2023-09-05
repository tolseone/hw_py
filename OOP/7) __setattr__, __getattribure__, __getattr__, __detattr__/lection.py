class Point:
    MAX_COORD = 100
    MIN_COORD = 0
 
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
 
    def __getattribute__(self, item):   # Автоматически вызывается, когда идет считывание атрибута через экземпляр класса. Например, при обращении к свойству MIN_COORD
        if item == "_Point__x": # явно запретим считывать такой атрибут из экземпляра класса
            raise ValueError("Private attribute")
        print("__getattribute__")  
        return object.__getattribute__(self, item)
    
    def __setattr__(self, key, value): # автоматически вызывается в момент присваивания атрибуту нового значения
        if key == "yy":
            raise AttributeError("Private attribute can only change by setter") # явно запретим изменять такой атрибут из экземпляра класса
        print(f"__setattr__ {key}")
        object.__setattr__(self, key, value)

    def __getattr__(self, item): # автоматически вызывается, если идет обращение к несуществующему атрибуту
        return False # в консоли выведется сообщение False, если такого атрибута не существует
    
    def __delattr__(self, item): #  вызывается в момент удаления какого-либо атрибута из экземпляра класса
        print("__delattr__: "+item)
        object.__delattr__(self, item)
    
pt1 = Point(1, 2)                                   # __setattr__ - присваивание переменных __x и __y
# print(pt1._Point__x)                              # __getattribute__

# pt1._Point__x = 10                                # __setattr__ - присваивание переменной __x значение 10

# print(pt1.z)                                      # __getattr__

# pt1.a = 10                                        # __delattr__ - удаление атрибута с возможностью вывода в консоль чего либо, либо запрет на удаление
# del pt1.a





