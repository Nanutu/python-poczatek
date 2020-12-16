# W klasie Order zastąp pole z łączną wartością zamówienia property typu getter,
# w ramach którego ta wartość będzie dynamicznie obliczana.
# Pozwoli to usunąć z konstruktora oraz napisanego w poprzednim zadaniu settera ponowne przeliczanie łącznej wartości zamówienia.


from shop.order import Order
from shop.data_generator import generate_order_elements


def run_homework():
    order_elements = generate_order_elements()
    normal_order = Order(client_first_name="Maciej", client_last_name="Xyz", order_elements=order_elements)
    print(normal_order)

    order_elements_2 = generate_order_elements(3)
    normal_order.order_elements = order_elements_2
    print(normal_order)

    order_elements_3 = generate_order_elements(1000)
    normal_order.order_elements = order_elements_3
    print(normal_order)

    print(normal_order.total_price)


if __name__ == '__main__':
    run_homework()
