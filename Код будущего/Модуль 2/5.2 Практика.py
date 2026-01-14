class Transport:
    def __init__(self, speed):
        self.speed = speed
        print ("Создан объект класса Tranport")

    def __str__(self):
        return f"Транспортное средство с максимальной скоростью {self.speed}"

    def move_up(self):
        self.speed = self.speed + 10
    
    def move_down(self):
        self.speed = self.speed - 10

class Car(Transport):
    def __init__(self,speed,color):
        super().__init__(speed)
        self.color = color

    def __str__(self):
        return f"{self.color} автомобиль с максимальной скоростью {self.speed}"

    def __add__(self, other):
        self.speed = self.speed + other.speed
        return self.speed
    
    def __eq__(self, other):
        if not (isinstance(other, Car)):
            print("not")
            return False
        if self.color == other.color and self.speed == other.speed:
            return True
        else:
            return False

a = Transport(100)
print(a.speed)
a.move_up()
print(a.speed)
a.move_down()
print(a.speed)
b = Car(200, "Yellow")
# b.move_up()
print(b.speed)
print(b.color)
print(b)
c = Car(200, "Yellow")
print(c)
print(b+c)
print(b==c)