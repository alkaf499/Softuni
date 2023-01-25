class Product:
    def __init__(self, name: str, quantity:int):
        self. name = name
        self.quantity = quantity

    def decrease(self, to_dec_quantity: int):
        if self.quantity - to_dec_quantity >= 0:
            self.quantity -= to_dec_quantity

    def increase(self, to_inc_quantity: int):
        self.quantity += to_inc_quantity

    def __str__(self):
        return self.name

