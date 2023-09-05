# Паттерн Singleton - всего может быть создан 1 экземпляр класса. При создании второго экземпляра класса, он будет являться ссылкой на первый и тд.

class DataBase:
    __instanse = None
    
    def __new__(cls, *args, **kwargs):
        if cls.__instanse is None:   # если экземпляров класса не существует, то __instanse примет значение нового экзепляра класса DataBase
            cls.__instanse = super().__new__(cls)   
        return cls.__instanse # возвращаем значение __instanse
    
    def __del__(self):    # Служит для того, чтобы при удалении экземпляра класса __instanse принимало значение None
        DataBase.__instanse = None

    def __init__(self, user, psw, port):
        self.user = user
        self.psw = psw
        self.port = port

    def connect(self):
        print(f"соединение с БД: {self.user}, {self.psw}, {self.port}")

    def close(self):
        print("закрытие соединения с БД")

    def read(self):
        return "данные из БД"
    
    def write(self, data):
        print(f"запись в БД {data}")

db = DataBase("tolseone", 2937, 80) #создание 1-ого объекта
db2 = DataBase("tolya", 228, 90) # создание 2-ого объекта
# db2 = 0 если вызвать эту команду, то объект db2 класса DataBase удалиться магическим методом __del__ класаса DataBase
print(id(db), id(db2)) # Если id одинаковые (а это так), то это говорит нам о том, что при попытке создания второго объекта он не был создан и ссылается на первый объект

db.connect() # Но без использования __call__ выведется информация, которая была введена при создании объекта db2
db2.connect() # Но без использования __call__ выведется информация, которая была введена при создании объекта db2