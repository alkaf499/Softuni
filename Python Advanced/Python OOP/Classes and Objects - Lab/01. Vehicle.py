class Vehicle:

    def __init__(self, mileage, max_speed = 150):
        self.mileage = mileage
        self.max_speed = max_speed
        self.gadgets = []

///
import unittest

class Tests(unittest.TestCase):
    def test_init(self):
        car = Vehicle(20)
        self.assertEqual(car.max_speed, 150)
        self.assertEqual(car.mileage, 20)
        self.assertEqual(car.gadgets, [])
    
    def test_add_gadget(self):
        car = Vehicle(20)
        car.gadgets.append('Hudly Wireless')
        self.assertEqual(car.gadgets, ['Hudly Wireless'])
        
if __name__ == "__main__":
    unittest.main()
