import view, model

def start():
    view.welcome()
    username = input("Как мне к вам обращаться?\n")
    while True:
        view.сontacting_the_user(username)
        view.menu()
        answer = input("Введите команду: ")
        if answer == "1":
            date = model.get_data()
            view.show_contacts(date)
        elif answer == "2":
            contact = input("Для того, чтобы создать новый контакт, введите\nФ И О и номер телефона через пробел: ")
            res = model.add_contact(contact)
            if res:
                view.succes(res)
            else:
                view.not_succes()
        elif answer == "3":
            info = input("Введите данные контакта для поиска: ")
            result = model.search(info)
            view.show_contacts(result)
        elif answer == "4":
            while True:
                view.submenu()
                user_response = input("Введите команду: ")
                if user_response == "1":
                    old_name = input("Введите данные, которые хотите заменить(в формате Ф И О номер телефона): ")
                    new_name = input("Введите новые данные для замены: ")
                    old_data, new_data = model.replace_data(old_name, new_name)
                    view.show_red_contacts(old_data, new_data)
                elif user_response == "2":
                    date = model.get_data()
                    view.show_contacts(date)
                elif user_response == "3":
                    break
                else:
                    view.error()
        elif answer == "5":
            info_for_delete = input("Введите Имя и номер телефона контакта через пробел, который вы хотите удалить: ").split()
            deleted_cont = model.delete_contact(info_for_delete)
            if len(deleted_cont) != 0:
                view.deleted_contact(deleted_cont)
            else:
                view.error_to_del_contact()
        elif answer == "6":
            view.goodbye()
            break
        else:
            view.error()