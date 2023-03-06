from unittest import TestCase, main

from project.vehicle import Vehicle


class TestmMamal(TestCase):
    def setUp(self):
        self.car = Vehicle(70.5, 150.5)

    def test_initialisation(self):
        self.assertEqual(70.5, self.car.fuel)
        self.assertEqual(70.5, self.car.capacity)
        self.assertEqual(150.5, self.car.horse_power)
        self.assertEqual(1.25, self.car.DEFAULT_FUEL_CONSUMPTION)

    def test_drive_not_enough_fuel_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.drive(10000)
        self.assertEqual('Not enough fuel', str(ex.exception))

    def test_drive_working_well(self):
        self.car.drive(1)
        self.assertEqual(69.25, self.car.fuel)

    def test_refuel_add_more_fuel_than_capacity_raise_execpt(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(10000)
        self.assertEqual('Too much fuel', str(ex.exception))

    def test_refuel_correct_amount(self):
        self.car.drive(10)
        self.car.refuel(10)
        self.assertEqual(68, self.car.fuel)

    def test_str(self):
        self.assertEqual("The vehicle has 150.5 horse power with 70.5 fuel left and 1.25 fuel consumption", self.car.__str__())



if __name__ == '__main__':
    main()
