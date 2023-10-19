# Подвиг 4. С помощью множественного наследования удобно описывать принадлежность объектов к нескольким разным группам. Выполним такой пример.

# Определите в программе классы в соответствии с их иерархией, представленной на рисунке выше:

# Digit, Integer, Float, Positive, Negative

# Каждый объект этих классов должен создаваться однотипной командой вида:

# obj = Имя_класса(value)
# где value - числовое значение. В каждом классе следует делать свою проверку на корректность значения value:

# - в классе Digit: value - любое число;
# - в классе Integer: value - целое число;
# - в классе Float: value - вещественное число;
# - в классе Positive: value - положительное число;
# - в классе Negative: value - отрицательное число.

# Если проверка не проходит, то генерируется исключение командой:

# raise TypeError('значение не соответствует типу объекта')
# После этого объявите следующие дочерние классы:

# PrimeNumber - простые числа; наследуется от классов Integer и Positive;
# FloatPositive - наследуется от классов Float и Positive.

# Создайте три объекта класса PrimeNumber и пять объектов класса FloatPositive с произвольными допустимыми для них значениями. Сохраните все эти объекты в виде списка digits.

# Затем, используя функции isinstance() и filter(), сформируйте следующие списки из указанных объектов:

# lst_positive - все объекты, относящиеся к классу Positive;
# lst_float - все объекты, относящиеся к классу Float.

# P.S. В программе требуется объявить только классы и создать списки. На экран выводить ничего не нужно.
from abc import abstractmethod, ABC

class Digit(ABC):
    def __init__(self, value):
        self._valid_data(value)
        self.value = value

    @staticmethod
    @abstractmethod
    def _valid_data(value):
        pass


class Integer(Digit):
    @staticmethod
    def _valid_data(value):
        if not isinstance(value, int):
            raise TypeError('значение не соответствует типу объекта')


class Float(Digit):
    @staticmethod
    def _valid_data(value):
        if not isinstance(value, float):
            raise TypeError('значение не соответствует типу объекта')

class Positive(Digit):
    @staticmethod
    def _valid_data(value):
        if not isinstance(value, (int, float)) or value < 0:
            raise TypeError('значение не соответствует типу объекта')

class Negative(Digit):
    @staticmethod
    def _valid_data(value):
        if not isinstance(value, (int, float)) or value >= 0:
            raise TypeError('значение не соответствует типу объекта')

class PrimeNumber(Integer, Positive):
    pass


class FloatPositive(Float, Positive):
    pass

digits = [PrimeNumber(3), PrimeNumber(1), PrimeNumber(4), FloatPositive(1.5), 
        FloatPositive(9.2), FloatPositive(6.3), FloatPositive(3.5), FloatPositive(8.9),]

lst_positive = [obj for obj in digits if isinstance(obj, Positive)]
lst_float = [obj for obj in digits if isinstance(obj, Float)]