from abc import ABC
class Vehicle(ABC):
    def __init__(self, cords, price, velocity, year):
        self.cords = cords
        self.price = price
        self.velocity = velocity
        self.year = year

    def view(self):
        return self.home_port

    def speed(self):
        self.price += 5


class Airliner(Vehicle):
    def __init__(self, cords, price, velocity, year, height, passenger):
        super(Airliner, self).__init__(cords, price, velocity, year)
        self.height = height
        self.passenger = passenger


class Car(Vehicle):
    def __init__(self, cords, price, velocity, year, passenger):
        super(Car, self).__init__(cords, price, velocity, year)
        self.passenger = passenger


class Ship(Vehicle):
    def __init__(self, cords, price, velocity, year, home_port):
        super(Ship, self).__init__(cords, price, velocity, year)
        self.home_port = home_port


airline = Airliner(0.5, 100000, 5, 2016, 120, 100)
car = Car(5, 5000, 5, 2021, 100)
ship = Ship(5, 20000, 4, 2012, 'Odessa')

print (ship.view())
