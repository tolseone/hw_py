# Подвиг 8. Объявите класс DeltaClock для вычисления разницы времен. Объекты этого класса должны создаваться командой:

# dt = DeltaClock(clock1, clock2)
# где clock1, clock2 - объекты другого класса Clock для хранения текущего времени. Эти объекты должны создаваться командой:

# clock = Clock(hours, minutes, seconds)
# где hours, minutes, seconds - часы, минуты, секунды (целые неотрицательные числа).

# В классе Clock также должен быть (по крайней мере) один метод (возможны и другие):

# get_time() - возвращает текущее время в секундах (то есть, значение hours * 3600 + minutes * 60 + seconds).

# После создания объекта dt класса DeltaClock, с ним должны выполняться команды:

# str_dt = str(dt)   # возвращает строку разницы времен clock1 - clock2 в формате: часы: минуты: секунды
# len_dt = len(dt)   # разницу времен clock1 - clock2 в секундах (целое число)
# print(dt)   # отображает строку разницы времен clock1 - clock2 в формате: часы: минуты: секунды
# Если разность получается отрицательной, то разницу времен считать нулевой.

# Пример использования классов (эти строчки в программе писать не нужно):

# dt = DeltaClock(Clock(2, 45, 0), Clock(1, 15, 0))
# print(dt) # 01: 30: 00
# len_dt = len(dt) # 5400
# Обратите внимание, добавляется незначащий ноль, если число меньше 10.

# P.S. На экран ничего выводить не нужно, только объявить классы.

class DeltaClock:
    def __init__(self, time1, time2):
        self._time1 = time1
        self._time2 = time2

    def __str__(self):
        tmp = self.__len__()
        h = tmp // 3600
        m = tmp % 3600 // 60
        s = tmp % 3600 % 60
        return f"{h:02}: {m:02}: {s:02}" # h:02 - значит, что у нас могут появится незначащиеся нули ( как нам и нужно)

    def __len__(self):
        difference = self._time1.get_time() - self._time2.get_time()
        return difference if difference > 0 else 0

class Clock:
    def __init__(self, hours, minutes, seconds):
        self._hours = hours
        self._minutes = minutes
        self._seconds = seconds
    
    def get_time(self):
        return self._hours * 3600 + self._minutes * 60 + self._seconds
    
t2 = Clock(1, 1, 1)
t1 = Clock(2, 1, 1)
pt = DeltaClock(t1, t2)
print(len(pt))
print(pt)