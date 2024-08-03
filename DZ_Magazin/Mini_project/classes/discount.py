class Discount:
    def __init__(self, description: str, discount_percent: float):
        self.description = description
        self.discount_percent = discount_percent

    @staticmethod
    def apply_discount(price, discount_percent):
        return price * (1 - discount_percent / 100)

    def __str__(self):
        return f"Скидка (Описание={self.description}, Процент={self.discount_percent})"

    def __repr__(self):
        return f"Discount(description={self.description}, discount_percent={self.discount_percent})"
