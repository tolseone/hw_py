# __getitem__(self, item) – получение значения по ключу item;
# __setitem__(self, key, value) – запись значения value по ключу key;
# __delitem__(self, key) – удаление элемента по ключу key.

class Student:
    def __init__(self, name: str, marks: list):
        self.name = name
        self.marks = list(marks)

    def __getitem__(self, item):
        if 0 <= item < len(self.marks):
            return self.marks[item]
        else:
            raise IndexError("Неверный индекс")
    
    def __setitem__(self, key, value):
        if not isinstance(key, int) or key < 0:
            raise TypeError("Индекс должен быть целым неотрицательным числом")
        
        if key >= len(self.marks):
            off = key + 1 - len(self.marks)
            self.marks.extend([None] * off)
        self.marks[key] = value

    def __delitem__(self, key):
        if not isinstance(key, int):
            raise TypeError("Индекс должен быть целым неотрицательным числом")
        
        del self.marks[key]
    


s1 = Student("tolseone", [5, 3, 5, 4, 5, 3])
print(s1[2])  # __getitem__ - для удобства обращения к элементу списка
s1[22] = 4     # __setitem__
del s1[1]     # __delitem__
print(s1.marks)
