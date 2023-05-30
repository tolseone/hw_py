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
    with open('phonebook.txt', 'r+', encoding='utf-8') as file:
        old_data = file.readlines()
        new_data = list()
        file.seek(0)
        old_lines, new_lines = list(), list()
        for line in old_data:
            if old_name in line:
                old_lines.append(line.strip())
                if len(old_name) < len(new_name):
                    line = line.replace(old_name, new_name) + ' '*(len(new_name) - len(old_name))
                elif len(old_name) > len(new_name):
                    line = line.replace(old_name, new_name) +' '*(len(old_name) - len(new_name) + 1)
                else:
                    line = line.replace(old_name, new_name)
                new_lines.append(line.strip())
                new_data.append(line)
            else:
                new_data.append(line)
        file.seek(0)
        file.writelines(new_data)
        return old_lines, new_lines
    
def delete_contact(info_for_delete: list):
    with open('phonebook.txt', 'r+', encoding='utf-8') as file:
        old_data = file.readlines()
        new_data = list()
        file.seek(0)
        deleted_line = list()
        for line in old_data:
            if all(words in line for words in info_for_delete):
                deleted_line.append(line.strip())
            else:
                new_data.append(line)
        file.seek(0)
        file.writelines(new_data)
        return deleted_line
