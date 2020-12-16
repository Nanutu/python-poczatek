# Dodaj do programu obsługę polityki rabatowej.
# Zaimplementuj funkcje reprezentujące politykę rabatową i przekaż je do konstruktora zamówienia.
# Jeżeli polityka została przekazana to podczas liczenia łącznej kwoty zamówienia należy naliczyć rabat.
# Jeżeli nie - obliczamy łączną kwotę jak dotychczas.
# Zaimplementuj dwie polityki rabatowe:
#
#     a) Dla stałych klientów: 5% rabatu na każdą pozycję
#     b) Rabat świąteczny: rabat 20 PLN dla zamówień o łącznej kwocie powyżej 100 PLN


import random
from shop.order import Order
from shop.discount_policy import loyal_customer_policy, christmas_policy
from shop.order_element import OrderElement
from shop.product import Product


def generate_order(products_number):
    order_elements = []
    for product_number in range(products_number):
        product_name = f"Produkt-{product_number}"
        category_name = "Inne"
        unit_price = random.randint(1, 30)
        product = Product(product_name, category_name, unit_price)
        quantity = random.randint(1, 10)
        order_elements.append(OrderElement(product, quantity))
    return order_elements


def run_homework():
    order_elements = generate_order(5)
    normal_order = Order(client_first_name="Maciej", client_last_name="Xyz", order_elements=order_elements)
    loyal_customer_order = Order(client_first_name="Maciej", client_last_name="Xyz", order_elements=order_elements,
                                 discount_policy=loyal_customer_policy)
    christmas_order = Order(client_first_name="Maciej", client_last_name="Xyz", order_elements=order_elements,
                            discount_policy=christmas_policy)

    print(normal_order)
    print(loyal_customer_order)
    print(christmas_order)


if __name__ == '__main__':
    run_homework()
