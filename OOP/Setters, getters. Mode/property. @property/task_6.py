# Реализуйте односвязный список (не список Python, не использовать список Python для хранения объектов), 
# когда один объект ссылается на следующий и так по цепочке до последнего:



# Для этого объявите в программе два класса: 

# StackObj - для описания объектов односвязного списка;
# Stack - для управления односвязным списком.

# Объекты класса StackObj предполагается создавать командой:

# obj = StackObj(данные)
# Здесь данные - это строка с некоторым содержимым. Каждый объект класса StackObj должен иметь следующие локальные приватные атрибуты:

# __data - ссылка на строку с данными, указанными при создании объекта;
# __next - ссылка на следующий объект класса StackObj (при создании объекта принимает значение None).

# Также в классе StackObj должны быть объявлены объекты-свойства:

# next - для записи и считывания информации из локального приватного свойства __next;
# data - для записи и считывания информации из локального приватного свойства __data.

# При записи необходимо реализовать проверку, что __next будет ссылаться на объект класса StackObj или значение None. Если проверка не проходит,
# то __next остается без изменений.

# Класс Stack предполагается использовать следующим образом:

# st = Stack() # создание объекта односвязного списка
# В объектах класса Stack должен быть локальный публичный атрибут:

# top - ссылка на первый добавленный объект односвязного списка (если список пуст, то top = None).

# А в самом классе Stack следующие методы:

# push(self, obj) - добавление объекта класса StackObj в конец односвязного списка;
# pop(self) - извлечение последнего объекта с его удалением из односвязного списка;
# get_data(self) - получение списка из объектов односвязного списка (список из строк локального атрибута __data каждого объекта в порядке их добавления,
#                                                                     или пустой список, если объектов нет).

# Пример использования классов Stack и StackObj (эти строчки в программе писать не нужно):

# st = Stack()
# st.push(StackObj("obj1"))
# st.push(StackObj("obj2"))
# st.push(StackObj("obj3"))
# st.pop()
# res = st.get_data()    # ['obj1', 'obj2']
# P.S. В программе требуется объявить только классы. На экран ничего выводить не нужно. 

class StackObj:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    @property
    def next(self):
        return self.__next
    
    @next.setter
    def next(self, obj):
        if self.is_valid(obj):
            self.__next = obj

    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, data):
        self.__data = data

    @staticmethod
    def is_valid(x):
        return type(x) is StackObj or x is None
    
class Stack:
    def __init__(self):
        self.top = None # ссылка на первый добавленный объект односвязного списка (если список пуст, то top = None).
        self.tail = None

    def push(self, obj):        # добавление объекта класса StackObj в конец односвязного списка;
        # if self.top is None:
        #     self.top = obj
        #     self.tail = obj
        # self.tail.next = obj
        # obj.next = None
        # self.tail = obj

        if self.tail:
            self.tail.next = obj
        
        obj.next = None
        self.tail = obj

        if self.top is None:
            self.top = obj

    def pop(self):              # извлечение последнего объекта с его удалением из односвязного списка;
        node = self.top
        if node is None:
            return
        while node and node.next != self.tail:
            node = node.next
        if node:
            node.next = None
        tail = self.tail 
        self.tail = node
        if self.tail is None:
            self.top = None
        return tail
    
    def get_data(self):         # получение списка из объектов односвязного списка (список из строк локального атрибута __data 
        s = []
        h = self.top
        while h:
            s.append(h.data)
            h = h.next
        return s

st = Stack()
st.push(StackObj("obj1"))
st.push(StackObj("obj2"))
st.push(StackObj("obj3"))
st.pop()
res = st.get_data()
print(res)