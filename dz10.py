import time
class Auto:
    def __init__(self, brand, age, mark, color=None, weight=None):
        self.brand = brand
        self.age = age
        self.color = color
        self.mark = mark
        self.weight = weight
    def move (self):
        print('move')
    def birthday  (self):
        return self.age+1
    def stop(self):
        print('stop')

class Truck(Auto):
    def __init__(self, brand, age, mark, max_load, color=None, weight=None):
        super().__init__(brand, age, mark, color, weight)
        self.max_load = max_load

    def move(self):
        print("attention")
        super().move()

    def load(self):
        time.sleep(1)
        print("load")
        time.sleep(1)

class Car(Auto):
    def __init__(self, brand, age, mark, max_speed,color=None, weight=None):
        super().__init__(brand, age, mark, color, weight)
        self.max_speed = max_speed

    def move(self):
        super().move()
        print(f'move, max speed is : {self.max_speed}')


truck1 = Truck('Tesla', 3, 'Model x', 1)
print(truck1.load())
print(truck1.move())
print(truck1.stop())
print(truck1.birthday())

truck2 = Truck('Porshe', 5, 'Cayenne', 4)
print(truck2.load())
print(truck2.move())
print(truck2.stop())
print(truck2.birthday())

car1 = Car('BMW', 7, 'x6', 3)
print(car1.move())
print(car1.birthday())
print(car1.stop())

car2 = Car('Mercedes', 2, 's666', 2)
print(car2.move())
print(car2.birthday())
print(car2.stop())