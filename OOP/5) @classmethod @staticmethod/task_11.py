#  Объявите класс для мессенджера с именем Viber. В этом классе должны быть следующие методы:

# add_message(msg) - добавление нового сообщения в список сообщений;
# remove_message(msg) - удаление сообщения из списка;
# set_like(msg) - поставить/убрать лайк для сообщения msg (т.е. изменить атрибут fl_like объекта msg: если лайка нет то он ставится, если уже есть, то убирается);
# show_last_message(число) - отображение последних сообщений;
# total_messages() - возвращает общее число сообщений.

# Эти методы предполагается использовать следующим образом (эти строчки в программе не писать):

# msg = Message("Всем привет!")
# Viber.add_message(msg)
# Viber.add_message(Message("Это курс по Python ООП."))
# Viber.add_message(Message("Что вы о нем думаете?"))
# Viber.set_like(msg)
# Viber.remove_message(msg)
# Класс Message (необходимо также объявить) позволяет создавать объекты-сообщения со следующим набором локальных свойств:

# text - текст сообщения (строка);
# fl_like - поставлен или не поставлен лайк у сообщения (булево значение True - если лайк есть и False - в противном случае, изначально False);

# P.S. Как хранить список сообщений, решите самостоятельно.

class Viber:
    messages = []
    @classmethod
    def add_message(cls, msg):
        cls.messages.append(msg)

    @classmethod
    def remove_message(cls, msg):
        cls.messages.remove(msg)

    @staticmethod
    def set_like(msg):
        msg.fl_like = not msg.fl_like # интересная конструкция

    @classmethod
    def show_last_message(cls, number):
        print(cls.messages[-number:]) # print(*[msg.text for msg in cls.msgs[-number:]]) # print(cls.messages[-number:])

    @classmethod
    def total_messages(cls):
        return len(cls.messages)


class Message:
    def __init__(self, text, fl_like=False):
        self.text = text
        self.fl_like = fl_like

msg = Message("Всем привет!")
Viber.add_message(msg)
Viber.add_message(Message("Это курс по Python ООП."))
Viber.add_message(Message("Что вы о нем думаете?"))
Viber.set_like(msg)
Viber.remove_message(msg)