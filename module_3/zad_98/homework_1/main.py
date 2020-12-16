# Wykorzystaj metodę super do odwołania się z poziomu klasy ExpressOrder do bazowej implementacji metody total_price i
# zastąp powtórzony w klasie potomnej algorytm wynikiem z tego odwołania.
#
# Pamiętaj, że łączna wartość zamówienia ekspresowego to:
# # łączna wartość zamówienia policzona według bazowej metody + opłata za ekspresową dostawę.

from shop.data_generator import generate_order_elements
from shop.discount_policy import PercentageDiscount, AbsoluteDiscount
from shop.order import Order
from shop.express_order import ExpressOrder


def run_homework():
    order_elements = generate_order_elements(11)
    five_percent_discount = PercentageDiscount(discount_percentage=5)
    hundred_pln_discount = AbsoluteDiscount(discount_value=100)

    order = Order(client_first_name="Maciej", client_last_name="Xyz", order_elements=order_elements)
    order_5_percent = Order(client_first_name="Maciej", client_last_name="Xyz", order_elements=order_elements,
                            discount_policy=five_percent_discount)
    order_100 = Order(client_first_name="Maciej", client_last_name="Xyz", order_elements=order_elements,
                      discount_policy=hundred_pln_discount)

    express_order = ExpressOrder(delivery_date="20th December 2020", client_first_name="Maciej",
                                 client_last_name="Sobieszuk", order_elements=order_elements)
    express_order_discount = ExpressOrder(delivery_date="20th December 2020", client_first_name="Maciej",
                                          client_last_name="Sobieszuk", order_elements=order_elements, discount_policy=hundred_pln_discount)

    print(order)
    print(order_5_percent)
    print(order_100)
    print(express_order)
    print(express_order_discount)


if __name__ == '__main__':
    run_homework()
