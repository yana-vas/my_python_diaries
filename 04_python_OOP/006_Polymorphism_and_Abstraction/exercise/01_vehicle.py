from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        self.fuel_consumption += 0.9
        needed_fuel_for_driving = self.fuel_consumption * distance
        if needed_fuel_for_driving > self.fuel_quantity:
            return
        self.fuel_quantity -= needed_fuel_for_driving

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        self.fuel_consumption += 1.6
        needed_fuel_for_driving = self.fuel_consumption * distance
        if needed_fuel_for_driving > self.fuel_quantity:
            return
        self.fuel_quantity -= needed_fuel_for_driving

    def refuel(self, fuel):
        self.fuel_quantity += (95*fuel)/100


car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)

truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)

