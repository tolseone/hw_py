def matrix(n=1, m=1, value=0):
    print([[value for _ in range(m)] for _ in range(n)])
# matrix(10, 10, 10)

def greet(*args):
    print(f"Hello, {args[0]}", end='')
    for i in range(1, len(args)):
        print(f" and {args[i]}", end='')
    print("!")
# greet('Timur', 'Roman', 'Ruslan')

def print_products(*args):
    list_products = [elem for elem in args if type(elem) is str and len(elem) > 0]
    if len(list_products) > 0:
        for i in range(1, len(list_products) + 1):
            print(f"{i}) {list_products[i - 1]}")
    else:
        print("Нет продуктов")

# print_products('Бананы', [1, 2], ('Stepik',), 'Яблоки', '', 'Макароны', 5, True)

def info_kwargs(**kwargs):
    for key, value in sorted(kwargs.items(), key = lambda para: para[0]):
        print(f"{key}: {value}")

info_kwargs(first_name='Timur', last_name='Guev', age=28, job='teacher')
