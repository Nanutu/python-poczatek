# 1.Rozbuduj rozwiązanie zadania drugiego z poprzedniej lekcji dodając funkcję, która będzie sprawdzać,
# których z zamówionych produktów jeszcze brakuje, po otrzymaniu kolejnej dostawy.

# 2.W tym celu najpierw zaimplementuj funkcję, products_delivery, która reprezentuje otrzymanie dostawy produktów.
#
# 3.Funkcja ta powinna zwracać listę produktów przywiezionych w ramach dostawy -
# w ramach symulacji niech wylosuje z powtórzeniami pięć nazw produktów
# (z listy dziesięciu dostępnych nazw produktów wylosuj pięć elementów ale tak,
# żeby mogły się one powtórzyć na liście wynikowej).

# 4.W skrypcie main najpierw “zamów dostawę”, a potem sprawdź, które produkty są jeszcze potrzebne.
#
# 5.Aby porównać otrzymane produkty z listą jeszcze potrzebnych wykorzystaj set.
#
# Następnie, tak długo realizuj kolejne zamówienia aż ostatecznie wszystkie z potrzebnych produktów zostaną dostarczone.


from shop.data_generator import generate_order_elements
from shop.discount_policy import PercentageDiscount, AbsoluteDiscount
from shop.order import Order
from shop.express_order import ExpressOrder
import random


available_products = [
        "product_1", "product_2", "product_3", "product_4", "product_5",
        "product_6", "product_7", "product_8", "product_9", "product_10"
    ]


def products_delivery():
    return [available_products[random.randint(0, 9)] for _ in range(5)]


def run_homework():
    needed_products = [
        "product_1", "product_2", "product_3", "product_4", "product_5",
        "product_6", "product_7", "product_8", "product_9", "product_10"
    ]
    received_products = []

    while set(received_products) != set(needed_products):
        new_products = products_delivery()
        print("Otrzymano: ", new_products)
        received_products += new_products
        missing_products = set(needed_products).difference(set(received_products))
        print("Brakuje:", missing_products)
    print(f"Łącznie otrzymano{received_products}")

    # order_elements = generate_order_elements()
    # print(order_elements)
    # identifier_to_product = {order_element.product.identifier: order_element.product for order_element in order_elements}
    # print(identifier_to_product)
    # identifier_to_product_2 = {identifier + 1: product for identifier, product in identifier_to_product.items()}
    # print(identifier_to_product_2)
    # identifier_to_product.update(identifier_to_product_2)
    # print(identifier_to_product)


if __name__ == '__main__':
    run_homework()
