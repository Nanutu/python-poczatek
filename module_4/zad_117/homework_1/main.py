# Do klasy Product dodaj pole identifier, będące liczbą.
#
# Następnie, zaktualizuj generator pozycji zamówienia, tak aby generował produkty zawierające losowy identyfikator.
#
# Użyj dict comprehensions, aby zamienić listę pozycji zamówienia w słownik,
# gdzie kluczem będzie identyfikator produktu z danej pozycji, a wartością będzie dany obiekt klasy Product.

from shop.data_generator import generate_order_elements
from shop.discount_policy import PercentageDiscount, AbsoluteDiscount
from shop.order import Order
from shop.express_order import ExpressOrder


def run_homework():
    order_elements = generate_order_elements()
    print(order_elements)
    identifier_to_product = {order_element.product.identifier: order_element.product for order_element in order_elements}
    print(identifier_to_product)


if __name__ == '__main__':
    run_homework()
