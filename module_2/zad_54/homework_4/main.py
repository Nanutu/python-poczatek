# Zaimplementuj metodę __eq__ dla klasy Product, Order Element oraz Order
# Dwa produkty są równe jeżeli mają taką samą nazwę, kategorię i cenę jednostkową
# Dwie pozycje w zamówieniu są równe jeżeli ilość jest równa oraz ich produkty są równe
# Dwa zamówienia są równe jeżeli zostały złożone przez tego samego klienta, mają taką samą liczbę pozycji
# i są one sobie równe (nie muszą znajdować się na tych samych miejscach na liście)


from shop.product import Product
from shop.order_element import OrderElement
from shop.order import Order


def run_homework():
    product_one = Product(name="Cookies", category_name="Food", unit_price=3.5)
    product_two = Product(name="Cheese", category_name="Food", unit_price=3.5)
    product_three = Product(name="Cookies", category_name="Food", unit_price=3.5)
    print(f"Products 1 and 2 are equal? {product_one == product_two}")
    print(f"Products 1 and 3 are equal? {product_one == product_three}")
    print(f"Products 2 and 3 are equal? {product_two == product_three}")

    order_element_1 = OrderElement(product_one, 3)
    order_element_2 = OrderElement(product_one, 3)
    order_element_3 = OrderElement(product_two, 4)
    print(f"Order elements 1 and 2 are equal? {order_element_1 == order_element_2}")
    print(f"Order elements 1 and 3 are equal? {order_element_1 == order_element_3}")
    print(f"Order elements 2 and 3 are equal? {order_element_2 == order_element_3}")

    order_1 = Order(client_first_name="Maciej", client_last_name="Sobieszuk",
                    order_elements=[order_element_1, order_element_2])
    order_2 = Order(client_first_name="Maciej", client_last_name="Sobieszuk",
                    order_elements=[order_element_2, order_element_1])
    order_3 = Order(client_first_name="Maciej", client_last_name="Xyz",
                    order_elements=[order_element_1, order_element_2])
    print(f"Orders 1 and 2 are equal? {order_1 == order_2}")
    print(f"Orders 1 and 3 are equal? {order_1 == order_3}")
    print(f"Orders 2 and 3 are equal? {order_2 == order_3}")


if __name__ == '__main__':
    run_homework()
