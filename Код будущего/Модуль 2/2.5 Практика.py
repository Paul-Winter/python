class Car:
    def __init__(self, speed, color='Yellow'):
        self.speed = speed
        self.color = color

car1 = Car(100)
car2 = Car(120, 'Red')

print(f'{car1.color} - {car1.speed}')
print(f'{car2.color} - {car2.speed}')