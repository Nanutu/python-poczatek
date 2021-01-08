# Zmodyfikuj obsługę przekroczenia dopuszczalnej liczby elementów zamówienia w klasie Order.
#
# W sytuacji, gdy przypisanie nowej listy elementów albo dodanie pozycji do zamówienia spowoduje
# przekroczenie limitu wyrzuć odpowiedni wyjątek.
#
# Przetestuj działanie programu w skrypcie main.


from shop.order import Order
from shop import data_generator


def run_example():
    order_elements = data_generator.generate_order_elements()
    order_1 = Order("Mac", "XYz", order_elements)
    print(order_1)
    product = data_generator.generate_product()
    quantity = data_generator.generate_quantity()
    order_1.add_product_to_order(product, quantity)
    print(order_1)


if __name__ == "__main__":
    run_example()
