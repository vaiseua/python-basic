
from homework_02.exceptions import LowFuelError, NotEnoughFuel
from abc import ABC

class Vehicle(ABC):

    weight = 1300
    started = False
    fuel = 50
    fuel_consumption = 15
    dist = 5

    def __init__(self, weight, fuel, fuel_consumption):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption


    def start(self):
        if self.fuel > 0:
            self.started = True
            return self.started
        else:
            raise LowFuelError()

    def move(self, dist):
        path = dist * self.fuel_consumption
        if self.fuel >= path:
            self.fuel -= path
            return self.fuel
        else:
            raise NotEnoughFuel()
