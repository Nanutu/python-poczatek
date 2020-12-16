# Dodaj do klasy Order maksymalną dopuszczalną liczbę elementów w zamówieniu.
#
# Upewnij się, że nie zostaje ona przekroczona podczas tworzenia obiektu klasy Order
# (w konstruktorze - gdy przekracza stwórz zamówienie tylko z pierwszymi X elementami)
# i podczas dodawania nowego produktu do zamówienia
# (gdy przekracza nie dodawaj produktu do zamówienia tylko wypisz informacje o przekroczeniu limitu).
#
# Żeby kontrolować liczbę pozycji w generowanym zamówieniu
# zastąp losową liczbę pozycji argumentem przekazanym do generate_order.


from shop.order import Order
from shop.product import Product


def run_homework():
    first_order = Order.generate_order(10)
    print(first_order)
    second_order = Order.generate_order(2)
    print(second_order)
    cookies = Product(name="Cookies", category_name="Food", unit_price=5)

    first_order.add_product_to_order(cookies, quantity=1)
    print(first_order)
    second_order.add_product_to_order(cookies, quantity=10)
    print(second_order)
    second_order.add_product_to_order(cookies, quantity=5)
    print(second_order)


if __name__ == '__main__':
    run_homework()
