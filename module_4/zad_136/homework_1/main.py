# Zastąp implementacje klas Product, ExpiringProduct oraz OrderElement dataclass.
#
# Zastanów się jaka jest korzyść z takiego podejścia w każdym z tych wariantów.
#
# A jak by to było w przypadku klasy Order?

from shop.order import Order
from shop.product import ExpiringProduct
from shop.data_generator import generate_order_elements


def run_homework():

    order_products = generate_order_elements()
    order = Order("Mac", "XYZ", order_products)
    print(order)


if __name__ == "__main__":
    run_homework()
