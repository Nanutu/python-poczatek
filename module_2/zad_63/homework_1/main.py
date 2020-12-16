# Zamień funkcję generate_order na metodę klasy Order.


from shop.order import generate_order, Order
from shop.product import Product


def run_homework():
    first_order = generate_order(10)
    print(first_order)
    second_order = generate_order(2)
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
