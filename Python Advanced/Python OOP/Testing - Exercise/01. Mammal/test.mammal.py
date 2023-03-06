from unittest import TestCase, main

from project.mammal import Mammal


class TestmMamal(TestCase):
    def setUp(self):
        self.mammal = Mammal('Catty', "Brown", "Meow")

    def test_correct_initialisation(self):
        self.assertEqual('Catty', self.mammal.name)
        self.assertEqual("Brown", self.mammal.type)
        self.assertEqual("Meow", self.mammal.sound)
        self.assertEqual("animals", self.mammal._Mammal__kingdom)

    def test_make_sound(self):
        result = self.mammal.make_sound()
        self.assertEqual("Catty makes Meow", result)

    def test_get_kingdom(self):
        result = self.mammal.get_kingdom()
        self.assertEqual('animals', result)

    def test_info(self):
        result = self.mammal.info()
        self.assertEqual('Catty is of type Brown', result)

if __name__ == '__main__':
    main()
