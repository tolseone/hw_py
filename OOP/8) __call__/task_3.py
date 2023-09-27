# Для последовательной обработки файлов из некоторого списка, например:

# filenames = ["boat.jpg", "web.png", "text.txt", "python.doc", "ava.8.jpg", "forest.jpeg", "eq_1.png", "eq_2.png", "my.html", "data.shtml"]
# Необходимо объявить класс ImageFileAcceptor, который бы выделял только файлы с указанными расширениями.

# Для этого предполагается создавать объекты класса командой:

# acceptor = ImageFileAcceptor(extensions)
# где extensions - кортеж с допустимыми расширениями файлов, например: extensions = ('jpg', 'bmp', 'jpeg').

# А, затем, использовать объект acceptor в стандартной функции filter языка Python следующим образом:

# image_filenames = filter(acceptor, filenames)
# Пример использования класса (эти строчки в программе писать не нужно):

# filenames = ["boat.jpg", "web.png", "text.txt", "python.doc", "ava.jpg", "forest.jpeg", "eq_1.png", "eq_2.png"]
# acceptor = ImageFileAcceptor(('jpg', 'bmp', 'jpeg'))
# image_filenames = filter(acceptor, filenames)
# print(list(image_filenames))  # ["boat.jpg", "ava.jpg", "forest.jpeg"]
# P.S. Ваша задача только объявить класс ImageFileAcceptor. На экран ничего выводить не нужно. 

class ImageFileAcceptor:
    def __init__(self, extensions):
        self.extensions = extensions

    def __call__(self, *args, **kwargs):
        if not isinstance(args[0], str):
            raise ValueError("Неверный тип данных")
        start = args[0].rfind('.')                              # extension = filename.split('.')[-1]
        ext = "" if start == -1 else args[0][start+1:]          # return extension in self._allowed_extensions  КРАСИВО!
        return ext in self.extensions
       
filenames = ["boat.jpg", "web.png", "text.txt", "python.doc", "ava.jpg", "forest.jpeg", "eq_1.png", "eq_2.png"]
acceptor = ImageFileAcceptor(('jpg', 'bmp', 'jpeg'))
image_filenames = filter(acceptor, filenames)
print(list(image_filenames))  # ["boat.jpg", "ava.jpg", "forest.jpeg"]