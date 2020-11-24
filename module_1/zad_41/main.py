from shop.apple import Apple
from shop.potato import Potato
from shop.product import Product
from shop.order import Order, random_order, print_order


def run_homework():
    apple_1 = Apple("ligol", size="A", price_per_kg=5)
    apple_2 = Apple("jonagold", size="B", price_per_kg=6)
    print(apple_1.species_name, apple_1)
    print(apple_2.species_name, apple_2)

    potato_1 = Potato("irys", size="B", price_per_kg=2)
    potato_2 = Potato("irga", size="C", price_per_kg=3)
    print(potato_1.species_name, potato_1)
    print(potato_2.species_name, potato_2)

    cookies = Product(name="Cookies", category_name="Food", unit_price=4)
    print(cookies)

    order_1 = Order(client_first_name="Jan", client_surname="Nowak", products=[cookies, cookies, cookies])
    print(order_1)
    order_2_empty = Order(client_first_name="Adam", client_surname="Kowal")
    print(order_2_empty)
    print_order(order_1)
    print_order(order_2_empty)

    order_random_1 = random_order()
    print_order(order_random_1)
    order_random_2 = random_order()
    print_order(order_random_2)


if __name__ == "__main__":
    run_homework()

