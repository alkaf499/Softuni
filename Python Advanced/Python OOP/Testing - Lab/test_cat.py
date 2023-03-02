class Cat:

  def __init__(self, name):
    self.name = name
    self.fed = False
    self.sleepy = False
    self.size = 0

  def eat(self):
    if self.fed:
      raise Exception('Already fed.')

    self.fed = True
    self.sleepy = True
    self.size += 1

  def sleep(self):
    if not self.fed:
      raise Exception('Cannot sleep while hungry')

    self.sleepy = False
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
