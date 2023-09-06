# Объявите класс SmartPhone, объекты которого предполагается создавать командой:

# sm = SmartPhone(марка смартфона)
# Каждый объект должен содержать локальные атрибуты:

# model - марка смартфона (строка);
# apps - список из установленных приложений (изначально пустой).

# Также в классе SmartPhone должны быть объявлены следующие методы:

# add_app(self, app) - добавление нового приложения на смартфон (в конец списка apps);
# remove_app(self, app) - удаление приложения по ссылке на объект app.

# При добавлении нового приложения проверять, что оно отсутствует в списке apps (отсутствует объект соответствующего класса).

# Каждое приложение должно определяться своим классом. Для примера объявите следующие классы:

# AppVK - класс приложения ВКонтаке;
# AppYouTube - класс приложения YouTube;
# AppPhone - класс приложения телефона.

# Объекты этих классов должны создаваться следующим образом (с соответствующим набором локальных атрибутов):

# app_1 = AppVK() # name = "ВКонтакте"
# app_2 = AppYouTube(1024) # name = "YouTube", memory_max = 1024
# app_3 = AppPhone({"Балакирев": 1234567890, "Сергей": 98450647365, "Работа": 112}) # name = "Phone", phone_list = словарь с контактами
# Пример использования классов (в программе эти строчки не писать):

# sm = SmartPhone("Honor 1.0")
# sm.add_app(AppVK())
# sm.add_app(AppVK())  # второй раз добавляться не должно
# sm.add_app(AppYouTube(2048))
# for a in sm.apps:
#     print(a.name)
# P.S. На экран ничего выводить не нужно. 

class SmartPhone:
    def __init__(self, model):
        self.model = model
        self.apps = []

    def add_app(self, app):
        if not tuple(filter(lambda x: type(x) == type(app), self.apps)):
            self.apps.append(app)

    def remove_app(self, app):
        if app in self.apps:
            self.apps.remove(app)

class AppVK:
    __instance = None
    def __new__(cls, *agrs, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance
    
    def __init__(self):
        self.name = "ВКонтакте"

class AppYouTube:
    __instance = None
    def __new__(cls, *agrs, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance
    
    def __init__(self, memomy_max):
        self.name = "YouTube"
        self.memory_max = memomy_max

class AppPhone:
    def __init__(self, *args):
        self.name = "Phone"
        self.phone_list = args

ph = AppPhone({"Балакирев": 1234567890, "Сергей": 98450647365, "Работа": 112})
sp = SmartPhone("xr")
sp.add_app(AppVK())
print(sp.__dict__)
print(ph.phone_list)