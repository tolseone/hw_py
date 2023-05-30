def get_data():
    with open('phonebook.txt', 'r', encoding = 'utf-8') as file:
        contacts = list(map(lambda line: line.strip(), file.readlines()))
        return contacts


def add_contact(contact):
    with open('phonebook.txt', 'a', encoding = 'utf-8') as file:
        file.write(contact)
        file.write('\n')
        return contact

def search(information_from_user: str):
    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        return[line.strip() for line in file if information_from_user in line]

def replace_data(old_name: str, new_name: str):
    # with open('phonebook.txt', 'r', encoding='utf-8') as file:
    #     old_data = file.read()
    # new_data = old_data.replace(old_name, new_name)

    # with open('phonebook.txt', 'w', encoding='utf-8') as file:
    #     file.write(new_data)
    # return[line for line in old_data]
    with open('phonebook.txt', 'r+', encoding='utf-8') as file:
        old_data = file.readlines()
        file.seek(0)
        old_lines, new_lines = list(), list()
        for line in old_data:
            if old_name in line:
                old_lines.append(line.strip())
                line = line.replace(old_name, new_name)
                new_lines.append(line.strip())
                file.write(line)
            else:
                file.write(line)
        return old_lines, new_lines
    
def delete_contact(info_for_delete: list):
    with open('phonebook.txt', 'r+', encoding='utf-8') as file:
        for line in file:
            count = 0
            for elems in info_for_delete:
                count += elems in line
            if count == len(info_for_delete):
                deleted_line = line
            else:
                file.write(line)
        return deleted_line
