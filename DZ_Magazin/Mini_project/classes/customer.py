class Customer:
    def __init__(self, name: str):
        self.name = name
        self.orders = []

    def add_order(self, order):
        self.orders.append(order)

    def total_spent(self):
        return sum(order.total_price() for order in self.orders)

    def __str__(self):
        return f"Клиент (Имя={self.name}, Заказы={len(self.orders)}, Потрачено={self.total_spent()})"

    def __repr__(self):
        return f"Customer(name={self.name})"
