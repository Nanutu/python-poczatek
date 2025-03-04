# Do klasy Order dodaj property typu setter, które będzie ustawiać listę pozycji w zamówieniu oraz
# aktualizować łączną wartość zamówienia (obliczaną na podstawie nowej listy pozycji).
#
# W setterze sprawdź również czy nowa lista elementów nie przekracza dopuszczalnej dla zamówienia ilości.
# Jeżeli przekracza, to przypisz do zamówienia tylko tyle pierwszych elementów z nowej listy,
# ile wynosi maksymalna dopuszczalna wartość w zamówieniu.


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


if __name__ == '__main__':
    run_homework()
