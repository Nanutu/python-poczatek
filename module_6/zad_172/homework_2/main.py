# W skrypcie main złap wyjątek rzucany przy przekroczeniu limitu zamówienia
# i wypisz prosty komunikat.

# Rozbuduj poprzednie rozwiązanie o wypisanie informacji zawartych w obiekcie wyjątku.


from shop.order import Order
from shop import data_generator
from shop.errors import OrderElementsLimitError


def run_example():
    order_elements = data_generator.generate_order_elements(number_of_products=Order.MAX_ORDER_ELEMENTS)
    order_1 = Order("Mac", "XYz", order_elements)
    print(order_1)

    product = data_generator.generate_product()
    quantity = data_generator.generate_quantity()

    try:
        order_1.add_product_to_order(product, quantity)
    except OrderElementsLimitError as error:
        print(f"Wystąpił błąd: >>{error}<<")
        print(f"Limit pozycji w zamówieniu wynosi: >>{error.places_limit}<<.")

    print(order_1)


if __name__ == "__main__":
    run_example()
