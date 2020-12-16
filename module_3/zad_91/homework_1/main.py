# Stwórz klasę ExpressOrder, która dziedziczy po klasie Order.
#
# Klasa ta będzie reprezentować zamówienie z ekspresowym terminem dostawy.
# Względem klasy Order powinna dodatkowo przyjmować informacje o terminie dostawy (jako data w postaci napisu)
# oraz naliczać dodatkową opłatę za ekspresową dostawę w ramach obliczania łącznego kosztu zamówienia.
#
# Zaktualizuj również metodę __str__ dodając do niej informacje o terminie dostawy.
#
# W skrypcie main stwórz obiekt klasy ExpressOrder i wypisz informacje o nim.


from shop.data_generator import generate_order_elements
from shop.discount_policy import christmas_policy
from shop.order import Order
from shop.express_order import ExpressOrder


def run_homework():
    order = generate_order_elements()

    express_order = ExpressOrder(delivery_date="20th December 2020", client_first_name="Maciej",
                                 client_last_name="Sobieszuk", order_elements=order)
    christmas_order = Order(client_first_name="Maciej", client_last_name="Xyz", order_elements=order,
                            discount_policy=christmas_policy)
    print(express_order)
    print(christmas_order)


if __name__ == '__main__':
    run_homework()
