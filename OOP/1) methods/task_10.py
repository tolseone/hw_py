# Дан класс Translator (для перевода с английского на русский), в котором объявлены три метода:
# class Translator:
#     def add(self, eng, rus):
#         if 'tr' not in self.__dict__:
#             self.tr = {}

#         self.tr.setdefault(eng, [])
#         # здесь продолжайте метод add
#     def remove(self, eng):
#         # здесь продолжайте метод remove

#     def translate(self, eng):
#         # здесь продолжайте метод translate
# В объекте этого класса должны локально (в атрибуте tr) храниться связки между английским и русскими словами в виде следующего словаря:
# {'<английское слово>': [<одно или несколько русских слов>], ...}
# Методы должны делать следующее:
# add(self, eng, rus) - для добавления в словарь новой связки английского и русского слова (если английское слово уже существует, то новое русское слово добавляется как синоним для перевода, например, go - идти, ходить, ехать); если связка eng-rus уже существует, то второй раз ее добавлять не нужно, например:  add('go', 'идти'), add('go', 'идти');
# remove(self, eng) - для удаления из словаря связки по указанному английскому слову;
# translate(self, eng) - для перевода с английского на русский (метод должен возвращать список из русских слов, 
# соответствующих переводу английского слова, даже если в списке всего одно слово).
# Все добавления и удаления связок должны выполняться внутри каждого конкретного объекта класса Translator, 
# т.е. связки хранить локально внутри экземпляров классов класса Translator, используя коллекцию-словарь. 
# (Хранить связки непосредственно в коллекции __dict__ не нужно!)
# Создайте экземпляр tr класса Translator и вызовите метод add для следующих связок:
# tree - дерево
# car - машина
# car - автомобиль
# leaf - лист
# river - река
# go - идти
# go - ехать
# go - ходить
# milk - молоко
# Затем методом remove() удалите связку для английского слова car. 
# С помощью метода translate() переведите слово go. Результат выведите на экран в виде строки из всех русских слов, связанных со словом go:
# Вывод в формате: идти ехать ходить

class Translator:
    def add(self, eng, rus):
        if 'tr' not in self.__dict__:
            self.tr = {}
        self.tr.setdefault(eng, [])
        if rus not in self.tr[eng]:
            self.tr[eng].append(rus)

        # здесь продолжайте метод add

    def remove(self, eng):
        self.tr.pop(eng, False)
        # здесь продолжайте метод remove

    def translate(self, eng):
        return self.tr[eng]
        # здесь продолжайте метод translate


tr = Translator()
for pair_of_words in ('tree - дерево', 'car - машина', 'car - автомобиль',
                      'leaf - лист', 'river - река', 'go - идти',
                      'go - ехать', 'go - ходить', 'milk - молоко'):
    tr.add(*pair_of_words.split(' - '))

tr.remove("car")
result = tr.translate("go")
print(*result)
# print(*tr.translate("go")) верхние 2 строчки в одну эту!