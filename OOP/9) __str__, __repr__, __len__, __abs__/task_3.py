# Подвиг 3. Объявите класс с именем Model, объекты которого создаются командой:

# model = Model()
# Объявите в этом классе метод query() для формирования записи базы данных. Использоваться этот метод должен следующим образом:

# model.query(field_1=value_1, field_2=value_2, ..., field_N=value_N)

# Например:

# model.query(id=1, fio='Sergey', old=33)
# Все эти переданные данные должны сохраняться внутри объекта model класса Model. Затем, при выполнении команды:

# print(model)
# В консоль должна выводиться информация об объекте в формате:

# "Model: field_1 = value_1, field_2 = value_2, ..., field_N = value_N"

# Например:

# "Model: id = 1, fio = Sergey, old = 33"

# Если метод query() не вызывался, то в консоль выводится строка:

# "Model"

# P.S. В программе нужно только объявить класс, выводить в консоль ничего не нужно.

class Model:
    def __init__(self):
        self.base = {}

    def query(self, **kwargs):
        for key, item in kwargs.items():
            self.base[key] = item

    def __str__(self):
        if not self.base:
            return f"Model"
        return f"Model: " + ''.join([f"{key} = {item}, " for key, item in self.base.items()])[:-2]

model = Model()
model.query(id=1, fio='Sergey', old=33)
print(model)