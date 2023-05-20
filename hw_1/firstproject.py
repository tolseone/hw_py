from random import *
print("Добро пожаловать в числовую угадайку!")

def is_valid(string):
    return string.isdigit() and 1 <= int(string) <= 100

def input_num():
    while True: 
        your_number = input('Введите число от 1 до 100: ')
        if is_valid(your_number):
            return int(your_number)
        else:
            print('А может быть все-таки введёшь целое число от 1 до 100?')

def compare_num():
    num, count = randint(1, 100), 0
    while True:
        n = input_num()
        if n > num:
            print("Ваше число больше загаданного, попробуйте еще разок")
            count += 1
        elif n < num:
            print("Ваше число меньше загаданного, попробуйте еще разок")
            count += 1
        else:
            print(f"Вы угадали число {num} за {count + 1} попыток, Поздравляем! Спасибо за игру! Всего хорошего!")
            break

compare_num()


