from project.product import Product


class Drink(Product):
    Quantity = 10
    def __init__(self, name: str):
        super().__init__(name, self.Quantity)
