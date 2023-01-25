from project.product import Product


class ProductRepository():
    def __init__(self):
        self.products = []


    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str):
        for product in self.products:
            if product_name == product.name:
                return product


    def remove(self, product_name):
        product = self.find(product_name)
        if product:
            self.products.remove(product)


    def __repr__(self):
        return '\n'.join([f"{product}: {product.quantity}" for product in self.products])


