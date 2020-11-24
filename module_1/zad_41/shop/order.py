import random
from .product import Product, print_product


class Order:
    def __init__(self, client_first_name, client_surname, products=None):
        self.client_first_name = client_first_name
        self.client_surname = client_surname
        if products is None:
            products = []
        self.products = products
        total_price = 0
        for product in products:
            total_price += product.unit_price
        self.total_price = total_price


def random_order():
    products = []
    random_number = random.randint(1, 10)
    for number in range(random_number):
        products.append(Product(f"Product-{number}", "Inne", number*3))
    order_random = Order(client_first_name="Los", client_surname="Owy", products=products)
    return order_random


def print_order(order):
    print("x" * 20)
    print(f"Zamówienie złożone przez: {order.client_first_name} {order.client_surname}.")
    print(f"O łącznej wartości: {order.total_price} zł.")
    print("Zamówinione produkty:")
    for product in order.products:
        print("\t", end="")
        print_product(product)
    print("x" * 20)
