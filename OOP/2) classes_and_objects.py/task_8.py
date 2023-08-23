# Объявите класс с именем TravelBlog и объявите в нем атрибут:
# total_blogs: 0
# Создайте экземпляр этого класса с именем tb1, сформируйте в нем два локальных свойства:
# name: 'Франция'
# days: 6
# Увеличьте значение атрибута total_blogs класса TravelBlog на единицу.
# Создайте еще один экземпляр класса TravelBlog с именем tb2, сформируйте в нем два локальных свойства:
# name: 'Италия'
# days: 5
# Увеличьте значение атрибута total_blogs класса TravelBlog еще на единицу.
# P.S. На экран ничего выводить не нужно.
class TravelBlog:
    total_blogs = 0
    
tb1 = TravelBlog()
atrs_1 = {
    'name': "Франция",
    "days": 6,
    }
[setattr(tb1, key, value) for key, value in atrs_1.items()]
TravelBlog.total_blogs += 1
tb2 = TravelBlog()
atrs_2 = {
    'name': "Италия",
    "days": 5,
    }
[setattr(tb2, key, value) for key, value in atrs_2.items()]
TravelBlog.total_blogs += 1
