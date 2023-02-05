from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, fuel_quantity, fuel_consumption):
        self. fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption
    @abstractmethod
    def drive(self, distance: float):
        pass

    @abstractmethod
    def refuel(self, fuel: float):
        pass


class Car(Vehicle):
    CONDITIONER = 0.9

    def drive(self, distance: float):
        consumption = distance * (self.fuel_consumption + Car.CONDITIONER)
        if self.fuel_quantity - consumption >= 0:
            self.fuel_quantity -= consumption

    def refuel(self, fuel: float):
       self.fuel_quantity += fuel



class Truck(Vehicle):
    CONDITIONER = 1.6

    def drive(self, distance: float):
        consumption = distance * (self.fuel_consumption + Truck.CONDITIONER)
        if self.fuel_quantity - consumption >= 0:
            self.fuel_quantity -= consumption

    def refuel(self, fuel: float):
          self.fuel_quantity += 0.95 * fuel
        
   ///
  
  # test car
import unittest

class VehiclesTests(unittest.TestCase):
    def test_first_zero(self):
        car = Car(20, 5)
        car.drive(3)
        self.assertEqual(car.fuel_quantity, 2.299999999999997)
        car.refuel(10)
        self.assertEqual(car.fuel_quantity, 12.299999999999997)


if __name__ == '__main__':
    unittest.main()
