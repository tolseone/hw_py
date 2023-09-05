# Вы создаете телефонную записную книжку. Она определяется классом PhoneBook. Объекты этого класса создаются командой:

# p = PhoneBook()
# А сам класс должен иметь следующий набор методов:

# add_phone(phone) - добавление нового номера телефона (в список);
# remove_phone(indx) - удаление номера телефона по индексу списка;
# get_phone_list() - получение списка из объектов всех телефонных номеров.

# Каждый номер телефона должен быть представлен классом PhoneNumber. Объекты этого класса должны создаваться командой:

# note = PhoneNumber(number, fio)
# где number - номер телефона (число) в формате XXXXXXXXXXX (одиннадцати цифр, X - цифра); fio - Ф.И.О. владельца номера (строка).

# В каждом объекте класса PhoneNumber должны формироваться локальные атрибуты:

# number - номер телефона (число);
# fio - ФИО владельца номера телефона.

# Необходимо объявить два класса PhoneBook и PhoneNumber в соответствии с заданием.

# Пример использования классов (эти строчки в программе писать не нужно):

# p = PhoneBook()
# p.add_phone(PhoneNumber(12345678901, "Сергей Балакирев"))
# p.add_phone(PhoneNumber(21345678901, "Панда"))
# phones = p.get_phone_list()
# P.S. В программе требуется объявить только классы. На экран ничего выводить не нужно. 

class PhoneBook:
    __instanse = None
    def __new__(cls, *args, **kwargs):
        if cls.__instanse is None:
            cls.__instanse = super().__new__(cls)
        return cls.__instanse
    
    def __init__(self):
        self.phonebook = []

    def add_phone(self, phone):
        if self.is_valid(phone):
            self.phonebook.append(phone)

    def remove_phone(self, indx):
        if indx > len(self.phonebook) - 1:
            raise IndexError("Элемента с таким индексом не существует")
        else:
            self.phonebook.pop(indx)

    def get_phone_list(self):
        return self.phonebook


    @staticmethod
    def is_valid(phone):
        return isinstance(phone, PhoneNumber)
    
class PhoneNumber:
    def __init__(self, number, fio):
        if self.is_valid(number, fio):
            self.number = number
            self.fio = fio

    @staticmethod
    def is_valid(number, fio):
        return all((type(number) is int, len(str(number)) == 11, type(fio) is str))
    
p = PhoneBook()
p.add_phone(PhoneNumber(12345678901, "Сергей Балакирев"))
p.add_phone(PhoneNumber(21345678901, "Панда"))
p.remove_phone(3)
phones = p.get_phone_list()

print(phones)
    
    