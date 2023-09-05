class Point3D:
    def __init__(self, x, y, z):
        self._x = x
        self._y = y # Здесь у нас формируются защищенные локальные свойства для создаваемого объекта класса Point3D
        self._z = z
                    #  Теперь представим, что согласно заданию координаты должны представляться исключительно целыми числами

    @classmethod
    def verify_coord(cls, coord):
        if type(coord) != int:
            raise TypeError("Координата должна быть целым числом")
        
    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self, coord):
        self.verify_coord(coord)
        self._x = coord

    @property
    def y(self):
        return self._y
    
    @y.setter
    def y(self, coord):
        self.verify_coord(coord)
        self._y = coord

    @property
    def z(self):
        return self._z
    
    @z.setter
    def z(self, coord):
        self.verify_coord(coord)
        self._z = coord

                        # Но, смотрите, в нашем классе Point3D получилось своеобразное дублирование: мы три раза прописывали объекты-свойства, 
                        # фактически, с одинаковым функционалом. Менялись только названия методов и локальных атрибутов. 
                        # Представьте, во что превратится описание этого класса, если нужно будет задать 10 и более таких объектов-свойств! 
                        # Программист во всем этом просто запутается, да и редактировать такую программу станет непросто. 
                        # Как можно все это оптимизировать? Здесь нам на помощь как раз и приходят дескрипторы.

### Вначале, что вообще такое дескрипторы? Это класс, который содержит или один магический метод __get__:
# class A: # non-data descriptor (дескриптор не данных)
#    def __get__(self, instance, owner): 
#        return ...
### Или класс, в котором дополнительно прописаны методы __set__ и/или __del__:

# class B: # data descriptor (дексриптор данных)
#     def __get__(self, instance, owner):
#         return ...
 
#     def __set__(self, instance, value):
#         ...
 
#     def __del__(self):
#         ...

class ReadIntX:
    def __set_name__(self, owner, name):
        self.name = "_x"
 
    def __get__(self, instance, owner):
        return getattr(instance, self.name)
    
class Integer:
    @classmethod
    def verify_coord(cls, coord):
        if type(coord) != int:
            raise TypeError("Значения координаты должны быть типа int")
        
    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        # return instance.__dict__[self.name]
        return getattr(instance, self.name)
    
    def __set__(self, instance, value):
        self.verify_coord(value)
        # instance.__dict__[self.name] = value
        setattr(instance, self.name, value)

class Point3D:
    x = Integer()
    y = Integer()
    z = Integer()
    xr = ReadIntX()

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    

p = Point3D(1, 2, 3)
p.__dict__["xr"] = 5
print(p.xr, p.__dict__)
    