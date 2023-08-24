# Объявите класс CardCheck для проверки корректности информации на пластиковых картах. Этот класс должен иметь следующие методы:

# check_card_number(number) - проверяет строку с номером карты и возвращает булево значение True, если номер в верном формате и False - в противном случае. 
# Формат номера следующий: XXXX-XXXX-XXXX-XXXX, где X - любая цифра (от 0 до 9).
# check_name(name) - проверяет строку name с именем пользователя карты. Возвращает булево значение True, если имя записано верно и False - в противном случае.
# Формат имени: два слова (имя и фамилия) через пробел, записанные заглавными латинскими символами и цифрами. Например, SERGEI BALAKIREV.

# Предполагается использовать класс CardCheck следующим образом (эти строчки в программе не писать):

# is_number = CardCheck.check_card_number("1234-5678-9012-0000")
# is_name = CardCheck.check_name("SERGEI BALAKIREV")
# Для проверки допустимых символов в классе должен быть прописан атрибут:

# CHARS_FOR_NAME = ascii_lowercase.upper() + digits
# Подумайте, как правильнее объявить методы check_card_number и check_name (декораторами @classmethod и @staticmethod).

# P.S. В программе только объявить класс. На экран ничего выводить не нужно.

from string import ascii_lowercase, digits

class CardCheck:
    CHARS_FOR_NAME = ascii_lowercase.upper() + digits

    @staticmethod
    def check_card_number(number):
        obj = number.split("-")
        return len(obj) == 4 and all(len(four_digits) == 4 and set(four_digits) <= set(digits) for four_digits in obj)
        

    @classmethod
    def check_name(cls, name):
        return len(name.split()) == 2 and set(name) <= set(cls.CHARS_FOR_NAME + " ")

is_number = CardCheck.check_card_number("1234-5678-9012-0000-1232")
is_name = CardCheck.check_name("SERGEI BALAKIREV")
print(is_name)
print(is_number)