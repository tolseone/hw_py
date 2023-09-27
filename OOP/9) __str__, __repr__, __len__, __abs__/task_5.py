# Подвиг 5. Объявите класс LinkedList (связный список) для работы со следующей структурой данных:

# Здесь создается список из связанных между собой объектов класса ObjList. Объекты этого класса создаются командой:

# obj = ObjList(data)
# где data - строка с некоторой информацией. Также в каждом объекте obj класса ObjList должны создаваться следующие локальные атрибуты:

# __data - ссылка на строку с данными;
# __prev - ссылка на предыдущий объект связного списка (если объекта нет, то __prev = None);
# __next - ссылка на следующий объект связного списка (если объекта нет, то __next = None).

# В свою очередь, объекты класса LinkedList должны создаваться командой:

# linked_lst = LinkedList()
# и содержать локальные атрибуты:

# head - ссылка на первый объект связного списка (если список пуст, то head = None);
# tail - ссылка на последний объект связного списка (если список пуст, то tail = None).

# А сам класс содержать следующие методы:

# add_obj(obj) - добавление нового объекта obj класса ObjList в конец связного списка;
# remove_obj(indx) - удаление объекта класса ObjList из связного списка по его порядковому номеру (индексу); индекс отсчитывается с нуля.

# Также с объектами класса LinkedList должны поддерживаться следующие операции:

# len(linked_lst) - возвращает число объектов в связном списке;
# linked_lst(indx) - возвращает строку __data, хранящуюся в объекте класса ObjList, расположенного под индексом indx (в связном списке).

# Пример использования классов (эти строчки в программе писать не нужно):

# linked_lst = LinkedList()
# linked_lst.add_obj(ObjList("Sergey"))
# linked_lst.add_obj(ObjList("Balakirev"))
# linked_lst.add_obj(ObjList("Python"))
# linked_lst.remove_obj(2)
# linked_lst.add_obj(ObjList("Python ООП"))
# n = len(linked_lst)  # n = 3
# s = linked_lst(1) # s = Balakirev
# P.S. На экран в программе ничего выводить не нужно. 

class LinkedList:
    def __init__(self):
        self.head = self.tail = None

    def add_obj(self, obj):
        obj.prev = self.tail
        if self.tail:
            self.tail.next = obj
        self.tail = obj

        if not self.head:
            self.head = obj

    def __get_obj_by_index(self, indx):
        h = self.head
        n = 0
        while h and n < indx:
            h = h.next
            n += 1
        return h
    
    def remove_obj(self, indx):
        obj = self.__get_obj_by_index(indx)
        if obj is None:
            return
        
        p, n = obj.prev, obj.next # Настраиваем связи
        if p:
            p.next = n
        if n:
            n.prev = p
        
        if self.head == obj: # Если obj ссылался на self.head, то надо перенастроить связи, то есть self.head теперь станет слеюущий элемент - n
            self.head = n

        if self.tail == obj: # # Если obj ссылался на self.tail, то надо перенастроить связи, то есть self.tail теперь станет предыдущий элемент - p
            self.tail = p
        

    def __len__(self):
        count = 0
        if self.head is None:
            return 0
        
        obj = self.head
        while True:
            count += 1
            if obj.next is None:
                return count
            obj = obj.next

    # def __call__(self, indx, *args, **kwargs): # Лучший вариант, ниже мой вариант
    #     obj = self.__get_obj_by_index(indx)
    #     return obj.data if obj else None
    
    def __call__(self, indx):
        count = 0
        obj = self.head
        while obj and count != indx:
            obj = obj.next
            count += 1
        if obj:
            return obj.data
        return None
    
class ObjList:
    def __init__(self, data):
        self.__data = ""
        self.data = data
        self.__prev = self.__next = None

    @property
    def next(self):
        return self.__next
    
    @next.setter
    def next(self, obj):
        if type(obj) in (ObjList, type(None)):
            self.__next = obj

    @property
    def prev(self):
        return self.__prev
    
    @prev.setter
    def prev(self, obj):
        if type(obj) in (ObjList, type(None)):
            self.__prev = obj

    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, value):
        if type(value) == str:
            self.__data = value

    