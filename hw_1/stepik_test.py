# объявление функции
def get_next_prime(num):
    while is_prime(num + 1) != True:
        num += 1
    return num
    
    
def is_prime(num):
    return len([i for i in range(1, num +1) if num % i == 0]) == 2

# считываем данные
n = int(input("kz"))

# вызываем функцию
print(get_next_prime(n))