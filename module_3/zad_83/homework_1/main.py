# Udostępnij elementy zamówienia tylko do odczytu, stosując property typu getter.
#
# Utwórz zamówienie i wypisz w pętli wszystkie jego elementy.


from shop.order import Order
from shop.discount_policy import loyal_customer_policy, christmas_policy
from shop.data_generator import generate_order_elements


def run_homework():
    order_elements = generate_order_elements(5)
    normal_order = Order(client_first_name="Maciej", client_last_name="Xyz", order_elements=order_elements)
    loyal_customer_order = Order(client_first_name="Maciej", client_last_name="Xyz", order_elements=order_elements,
                                 discount_policy=loyal_customer_policy)
    christmas_order = Order(client_first_name="Maciej", client_last_name="Xyz", order_elements=order_elements,
                            discount_policy=christmas_policy)

    print(normal_order)
    for element in normal_order.order_elements:
        print(element)
    print(loyal_customer_order)
    print(christmas_order)


if __name__ == '__main__':
    run_homework()
