def welcome():
    print("Приветствую, Пользователь!", end=' ')

def goodbye():
    print("Программа завершает работу.\nВозвращайтесь снова!")

def сontacting_the_user(username: str):
    print(f'----------------------------\n{username.capitalize()}, что для вас сделать?')

def menu():
    print(
        '1 - Показать все контакты\n'
        '2 - Добавить контакт\n'
        '3 - Найти контакт\n'
        '4 - Отредактировать контакт\n'
        '5 - Удалить контакт\n'
        '6 - Выход'
    )

def error():
    print("Ошибка, введённой команды не существует.")

def show_contacts(date: list):
    print(*date, sep='\n')

def succes(res):
    print(f'Контакт создан успешно!\n{res}')

def not_succes():
    print("Контакт не создан. Вы не ввели данные.")

def submenu():
    print(
        '1 - Изменить Фамилию, Имя, Отчество, Телефон\n'
        '2 - Вывести список всех контактов\n'
        '3 - Вернуться в основное меню'
    )

def show_red_contacts(old: list, new: list):
    print("Контакты: ", *old, sep='\n')
    print("Заменены на: ",*new, sep='\n')

def deleted_contact(deleted_contact):
    print(f'Успешное удаление контакта:\n{deleted_contact}')

def error_to_del_contact():
    print("Ошибка! контакта с такими данными не существует.")

def error_to_red():
    print(
        'Ошибка при попытке редактирования контакта.\n'
        'Пожалуйста введите правильные данные.\n'
        'Число элементов, подлежащих замене должно быть равно числу заменяемых'
    )

# if __name__ == "__main__":
#     menu()