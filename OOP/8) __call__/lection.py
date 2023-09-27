import math

class Counter:
    def __init__(self):
        self.__counter = 0

    def __call__(self, step=1, *args, **kwargs):
        print("__call__")
        self.__counter += step
        return self.__counter
    
    # __call__(self, *args, **kwargs):                  # Упрощённая схема реализации метода __call__, в действительности, она несколько сложнее, 
    #   obj = self.__new__(self, *args, **kwargs)       # но принцип тот же: сначала вызывается магический метод __new__ для создания самого объекта 
    #   self.__init__(self, *args, **kwargs)            # в памяти устройства, а затем, метод __init__ - для его инициализации. То есть, класс можно 
    #   return obj                                      # вызывать подобно функции благодаря встроенной для него реализации магического метода __call__.
    
c = Counter()
c(3)
c(-2)
res = c(10)
                # Мы здесь три раза вызвали метод __call__ и счетчик __counter трижды увеличился на единицу. 
                # Поэтому в консоли мы видим значение 3. Мало того, если создать еще один объект-счетчик:
                # То они будут работать совершенно независимо и подсчитывать число собственных вызовов.
c = Counter()
c2 = Counter()
c2(-8)
res2 = c2(10)
print(res, res2)

                    # Примеры использования метода __call__

# Первый пример – это использование класса с методом __call__ вместо замыканий функций. 
# Мы можем объявить класс StripChars, который бы удалял вначале и в конце строки заданные символы:

class StripChars:
    def __init__(self, chars):
        self.__chars = chars

    def __call__(self, *args, **kwargs):
        if not isinstance(args[0], str):
            raise ValueError("Аргумент должен быть строкой")

        return args[0].strip(self.__chars) 
    
s1 = StripChars(" !")
res = s1(" Hello World! ")

s2 = StripChars("1234")
res2 = s2("12Hello World!4321")

print(res, res2, sep='\n')

# Второй пример – это реализация декораторов с помощью классов.

class Derivate:
    def __init__(self, func): # Здесь в инициализаторе сохраняем ссылку на функцию, которую декорируем.
        self.__fn = func
 
    def __call__(self, x, dx=0.0001, *args, **kwargs): # Принимает один обязательный параметр x – точку, где вычисляется производная и dx – шаг изменения при вычислении производной.
        return (self.__fn(x + dx) - self.__fn(x)) / dx
    
def df_sin(x):
    return math.sin(x)

# 1-ый вариант использования
df_sin = Derivate(df_sin)
print(df_sin(math.pi/3)) # Производная, если ранее был создан объект класса Derivate

# 2-ой вариант использования
@Derivate  # класс Декоратор Derivate
def df_sin(x):
    return math.sin(x)

print(df_sin(math.pi/3))

