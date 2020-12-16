# Zmodyfikuj rozwiązanie poprzedniego zadania.
#
# Skorzystaj z dict comprehensions, aby na podstawie słownika z produktami stworzyć nowy,
# w którym każdy produkt będzie pod kluczem o 1 większym.
#
# I tak produkt, który znajdował się w oryginalnym słowniku pod kluczem 15 trafi w nowym pod klucz 16, itd.
#
# Następnie skorzystaj z metody update aby “połączyć” oba słowniki.

from shop.data_generator import generate_order_elements
from shop.discount_policy import PercentageDiscount, AbsoluteDiscount
from shop.order import Order
from shop.express_order import ExpressOrder


def run_homework():
    order_elements = generate_order_elements()
    print(order_elements)
    identifier_to_product = {order_element.product.identifier: order_element.product for order_element in order_elements}
    print(identifier_to_product)
    identifier_to_product_2 = {identifier + 1: product for identifier, product in identifier_to_product.items()}
    print(identifier_to_product_2)
    identifier_to_product.update(identifier_to_product_2)
    print(identifier_to_product)


if __name__ == '__main__':
    run_homework()
