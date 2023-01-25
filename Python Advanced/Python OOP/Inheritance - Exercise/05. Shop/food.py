from project.product import Product


class Food(Product):
    Quantity = 15
    def __init__(self, name: str):
        super().__init__(name, self.Quantity)

