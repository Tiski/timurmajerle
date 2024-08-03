from classes.product import Product

class Order:
    _total_orders = 0

    def __init__(self, products: list):
        self.products = products
        Order._total_orders += 1

    @staticmethod
    def calculate_discounted_price(price, discount):
        return price * (1 - discount / 100)

    @classmethod
    def total_orders(cls):
        return cls._total_orders

    def total_price(self):
        return sum(product.price for product in self.products)

    def __str__(self):
        return f"Заказ (Общая цена = {self.total_price()})"

    def __repr__(self):
        return f"Order(total_price={self.total_price()})"
