import random
from shop.product import Product, ProductCategory
from shop.order_element import OrderElement
from shop.order import Order

MIN_UNIT_PRICE = 1
MAX_UNIT_PRICE = 30

MIN_PRODUCT_QUANTITY = 1
MAX_PRODUCT_QUANTITY = 10

MIN_IDENTIFIER = 1
MAX_IDENTIFIER = 100


def generate_order_elements(number_of_products=None):
    order_elements = []

    if number_of_products is None:
        number_of_products = random.randint(1, Order.MAX_ORDER_ELEMENTS)
    elif number_of_products > Order.MAX_ORDER_ELEMENTS:
        number_of_products = Order.MAX_ORDER_ELEMENTS

    for product_number in range(number_of_products):
        product_name = f"Produkt-{product_number}"
        category = ProductCategory.OTHER
        unit_price = random.randint(MIN_UNIT_PRICE, MAX_UNIT_PRICE)
        identifier = random.randint(MIN_IDENTIFIER, MAX_IDENTIFIER)
        product = Product(product_name, category, unit_price, identifier)
        quantity = random.randint(MIN_PRODUCT_QUANTITY, MAX_PRODUCT_QUANTITY)
        order_elements.append(OrderElement(product, quantity))

    return order_elements
