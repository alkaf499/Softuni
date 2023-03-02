class Worker:

    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'

//
from unittest import TestCase, main


class WorkerTests(TestCase):
    def setUp(self):
        self.worker = Worker("Alex", 1000, 100)

    def test_correct_initia(self):
        self.assertEqual("Alex", self.worker.name)
        self.assertEqual(1000, self.worker.salary)
        self.assertEqual(100, self.worker.energy)
        self.assertEqual(0, self.worker.money)

    def test_work__increment_salary(self):
        self.worker.work()
        self.assertEqual(self.worker.salary, self.worker.money)

    def test_work_energy(self):
        self.worker.work()
        self.assertEqual(99, self.worker.energy)

    def test_rest_energy_increment(self):
        self.worker.rest()
        self.assertEqual(101, self.worker.energy)

    def test_get_info(self):
        self.assertEqual("Alex has saved 0 money.", self.worker.get_info())

    def test_worker_with_zero_or_less_energy(self):
        self.worker.energy = 0
        with self.assertRaises(Exception) as ex:
            self.worker.work()
        self.assertEqual('Not enough energy.', str(ex.exception))


if __name__ == '__main__':
    main()
