# Объявите класс EmailValidator для проверки корректности email-адреса. Необходимо запретить создание объектов этого класса: 
# при создании экземпляров должно возвращаться значение None, например:

# em = EmailValidator() # None
# В самом классе реализовать следующие методы класса (@classmethod):

# get_random_email(cls) - для генерации случайного email-адреса по формату: xxxxxxx...xxx@gmail.com, где x - любой допустимый символ в email 
# (латинский буквы, цифры, символ подчеркивания и точка);
# check_email(cls, email) - возвращает True, если email записан верно и False - в противном случае.

# Корректность строки email определяется по следующим критериям:

# - допустимые символы: латинский алфавит, цифры, символы подчеркивания, точки и собачка @ (одна);
# - длина email до символа @ не должна превышать 100 (сто включительно);
# - длина email после символа @ не должна быть больше 50 (включительно);
# - после символа @ обязательно должна идти хотя бы одна точка;
# - не должно быть двух точек подряд.

# Также в классе нужно реализовать приватный статический метод класса:

# is_email_str(email) - для проверки типа переменной email, если строка, то возвращается значение True, иначе - False.

# Метод is_email_str() следует использовать в методе check_email() перед проверкой корректности email. Если параметр email не является строкой, 
# то check_email() возвращает False.

# Пример использования класса EmailValidator (эти строчки в программе писать не нужно):

# res = EmailValidator.check_email("sc_lib@list.ru") # True
# res = EmailValidator.check_email("sc_lib@list_ru") # False
# P.S. В программе требуется объявить только класс. На экран ничего выводить не нужно. 
from string import ascii_letters, digits
from random import sample, randint, randrange, choice
class EmailValidator:
    LETTER = ascii_letters + digits + "._"
    def __new__(cls):
        return None
    
    @classmethod
    def get_random_email(cls):
        first_part = [choice(cls.LETTER) for _ in range(randint(1, 101))]
        second_part = [choice(cls.LETTER) for _ in range(randint(1, 51))]
        result = "".join(list(map(str, first_part))) + "@" + "".join(list(map(str, second_part)))
        return result
    
    @classmethod
    def check_email(cls, email):
        if not cls.__is_email_str(email):
            return False
        if email.count("@") != 1:
            return False
        indx = email.index("@")
        if all([len(email[0:indx]) <= 100, len(email[indx+1:]) <= 50, ".." not in email, list(filter(lambda char: char == ".", email[indx + 1:]))]):
            return True
        return False
    
    @staticmethod
    def __is_email_str(email):
        return type(email) == str
    
em = EmailValidator()
print(EmailValidator.get_random_email())
print(EmailValidator.check_email("sc_lib@list_ru"))