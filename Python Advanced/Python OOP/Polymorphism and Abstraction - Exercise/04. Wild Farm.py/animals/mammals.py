from project.animals.animal import Mammal
from project.food import Vegetable, Fruit, Meat


class Mouse(Mammal):

    def __init__(self, name, weight: float, living_region: str):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Squeak"

    @property
    def food_that_eats(self):
        return [Vegetable, Fruit]

    @property
    def gained_weight(self):
        return 0.10


class Dog(Mammal):
    def __init__(self, name, weight: float, living_region: str):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Woof!"

    @property
    def food_that_eats(self):
        return [Meat]

    @property
    def gained_weight(self):
        return 0.40

class Cat(Mammal):
    def __init__(self, name, weight: float, living_region: str):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Meow"

    @property
    def food_that_eats(self):
        return [Vegetable, Meat]

    @property
    def gained_weight(self):
        return 0.30


class Tiger(Mammal):
    def __init__(self, name, weight: float, living_region: str):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "ROAR!!!"

    @property
    def food_that_eats(self):
        return [Meat]

    @property
    def gained_weight(self):
        return 1.00
