# Объявите пустой класс с именем Car. С помощью функции setattr() добавьте в этот класс атрибуты:
# model: "Тойота"
# color: "Розовый"
# number: "П111УУ77"
# Выведите на экран значение атрибута color, используя словарь __dict__ класса Car.
class Car:
    pass

dict_car = {
    'model': "Тойота",
    'color': "Розовый",
    'number': "П111УУ77",
    }
for name, value in dict_car.items():
    setattr(Car, name, value)

print(Car.__dict__['color'])
