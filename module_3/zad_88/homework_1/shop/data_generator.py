import random
from shop.product import Product
from shop.order_element import OrderElement
from shop.order import Order

MIN_UNIT_PRICE = 1
MAX_UNIT_PRICE = 30

MIN_PRODUCT_QUANTITY = 1
MAX_PRODUCT_QUANTITY = 10


def generate_order_elements(number_of_products=None):
    order_elements = []
    if number_of_products is None:
        number_of_products = Order.MAX_ORDER_ELEMENTS
    for product_number in range(number_of_products):
        product_name = f"Produkt-{product_number}"
        category_name = "Inne"
        unit_price = random.randint(MIN_UNIT_PRICE, MAX_UNIT_PRICE)
        product = Product(product_name, category_name, unit_price)
        quantity = random.randint(MIN_PRODUCT_QUANTITY, MAX_PRODUCT_QUANTITY)
        order_elements.append(OrderElement(product, quantity))
    return order_elements
