import sys
import os

# Добавляем путь к директории classes
sys.path.append(os.path.join(os.path.dirname(__file__), 'classes'))

from classes.product import Product
from classes.customer import Customer
from classes.order import Order
from classes.discount import Discount

# Создаем продукты
product1 = Product("Laptop", 1000)
product2 = Product("Smartphone", 500)
product3 = Product("Tablet", 300)
product4 = Product("Headphones", 100)
product5 = Product("Smartwatch", 200)

# Создаем клиентов
customer1 = Customer("Alice")
customer2 = Customer("Bob")
customer3 = Customer("Charlie")

# Создаем заказы и добавляем их к клиентам
order1 = Order([product1, product4])
order2 = Order([product2, product3])
order3 = Order([product1, product2, product3])
order4 = Order([product5, product4])
order5 = Order([product2, product3, product5])

customer1.add_order(order1)
customer1.add_order(order2)
customer2.add_order(order3)
customer2.add_order(order4)
customer3.add_order(order5)

# Применяем различные виды скидок
discount1 = Discount("Seasonal Discount", 10)
discount2 = Discount("Promo Code", 15)

order1_discounted_price = Discount.apply_discount(order1.total_price(), discount1.discount_percent)
order2_discounted_price = Discount.apply_discount(order2.total_price(), discount2.discount_percent)
order3_discounted_price = Discount.apply_discount(order3.total_price(), discount1.discount_percent)
order4_discounted_price = Discount.apply_discount(order4.total_price(), discount2.discount_percent)
order5_discounted_price = Discount.apply_discount(order5.total_price(), discount1.discount_percent)

# Выводим общую информацию о заказах
print(f"Сниженная цена на заказ 1: {order1_discounted_price}")  # Пример вывода: Сниженная цена на заказ 1: 990.0
print(f"Сниженная цена на заказ 2: {order2_discounted_price}")  # Пример вывода: Сниженная цена на заказ 2: 850.0
print(f"Сниженная цена на заказ 3: {order3_discounted_price}")  # Пример вывода: Сниженная цена на заказ 3: 1530.0
print(f"Сниженная цена на заказ 4: {order4_discounted_price}")  # Пример вывода: Сниженная цена на заказ 4: 255.0
print(f"Сниженная цена на заказ 5: {order5_discounted_price}")  # Пример вывода: Сниженная цена на заказ 5: 850.0

# Выводим общее количество заказов
print(f"Всего заказов: {Order.total_orders()}")  # Пример вывода: Всего заказов: 5

# Подсчитываем общую сумму всех заказов для всех клиентов
total_sum = sum(customer.total_spent() for customer in [customer1, customer2, customer3])
print(f"Общая сумма всех заказов для всех клиентов: {total_sum}")  # Пример вывода: Общая сумма всех заказов для всех клиентов: 4200

# Выводим информацию о клиентах и их заказах
print(customer1)  # Пример вывода: Клиент (Имя=Alice, Заказы=2, Потрачено=2100)
print(customer2)  # Пример вывода: Клиент (Имя=Bob, Заказы=2, Потрачено=1400)
print(customer3)  # Пример вывода: Клиент (Имя=Charlie, Заказы=1, Потрачено=700)

# Выводим информацию о заказах
print(order1)     # Пример вывода: Заказ (Общая цена = 1100)
print(order2)     # Пример вывода: Заказ (Общая цена = 1000)
print(order3)     # Пример вывода: Заказ (Общая цена = 1800)
print(order4)     # Пример вывода: Заказ (Общая цена = 300)
print(order5)     # Пример вывода: Заказ (Общая цена = 1000)

# Выводим информацию о продуктах
print(product1)   # Пример вывода: Продукт (Название=Laptop, Цена=1000)
print(product2)   # Пример вывода: Продукт (Название=Smartphone, Цена=500)
print(product3)   # Пример вывода: Продукт (Название=Tablet, Цена=300)
print(product4)   # Пример вывода: Продукт (Название=Headphones, Цена=100)
print(product5)   # Пример вывода: Продукт (Название=Smartwatch, Цена=200)
