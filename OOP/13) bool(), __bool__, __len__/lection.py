# __len__() - вызывается функцией bool(), если не определён маг. метод __bool__()
# __bool__() - вызывается в приоритетном порядке функцией bool()

# bool(123) -> True
# bool(0) -> False
# bool("Python") -> True
# bool("") -> False

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __len__(self):
        print("Вызов метода: __len__")
        return self.x ** 2 + self.y ** 2
    
    def __bool__(self):
        print("Вызов метода: __bool__")
        return self.x == self.y


p = Point(0, 0)
print(bool(p)) # bool всегда возвращается true для объектов класса, однако можем поменять поведение методами __len__ и __bool__
# Теперь, при определении метода __len__ , если результат даёт 0 - то bool вернёт False

# При определении метода __bool__, он работает В ПРИОРИТЕТЕ от метода __len__ 
# !!!!!!!!! __bool__ имеет больший приоритет чем __len__!!!!!!!!!!!!!

if p:
    print("объект p даёт True")
else:
    print("False")


