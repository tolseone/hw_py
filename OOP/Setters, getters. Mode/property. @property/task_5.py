# Объявите в программе класс WindowDlg, объекты которого предполагается создавать командой:

# wnd = WindowDlg(заголовок окна, ширина, высота)
# В каждом объекте класса WindowDlg должны создаваться приватные локальные атрибуты:

# __title - заголовок окна (строка);
# __width, __height - ширина и высота окна (числа).

# В классе WindowDlg необходимо реализовать метод:

# show() - для отображения окна на экране (выводит в консоль строку в формате: "<Заголовок>: <ширина>, <высота>", например "Диалог 1: 100, 50").

# Также в классе WindowDlg необходимо реализовать два объекта-свойства:

# width - для изменения и считывания ширины окна;
# height - для изменения и считывания высоты окна.

# При изменении размеров окна необходимо выполнять проверку:

# - переданное значение является целым числом в диапазоне [0; 10000].

# Если хотя бы один размер изменился (высота или ширина), то следует выполнить автоматическую перерисовку окна (вызвать метод show()). 
# При начальной инициализации размеров width, height вызывать метод show() не нужно.

# P.S. В программе нужно объявить только класс с требуемой функциональностью.

class WindowDlg:
    def __init__(self, title, width, height):
        self.__title = title
        self.__width = width
        self.__height = height

    def show(self):
        print(f"{self.__title}: {self.__width}, {self.__height}")

    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self, width):
        if self.is_valid(width):
            self.__width = width
            self.show()

    @property
    def height(self):
        return self.__height
    
    @height.setter
    def height(self, height):
        if self.is_valid(height):
            self.__height = height
            self.show()

    @staticmethod
    def is_valid(x):
        return type(x) is int and 0 <= x <= 10**4
    
w1 = WindowDlg("Заголовок:", 144, 256)
w1.height = 400