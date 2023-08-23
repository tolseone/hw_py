class Point:
    color = "red"
    circle = 2

    def __init__(self, x, y=10):
        self.x = x
        self.y = y

    def __del__(self):
        print(f"Удаление экземпляра: {str(self)}")
        
    def set_coords(self, x, y):
        self.x = x # локальное свойство
        self.y = y # локальное свойство

    def get_coords(self):
        return (self.x, self.y)
    

# pt = Point()
# pt.set_coords(1, 2)
# print(pt.__dict__)

pt = Point(1, y=11)
# pt.set_coords(10, 20)
print(pt.__dict__)
