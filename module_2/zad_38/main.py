class Product:
    pass


class Order:
    pass


class Apple:
    pass


class Potato:
    pass


if __name__ == "__main__":
    apple_1 = Apple()
    apple_2 = Apple()
    potato_1 = Potato()
    potato_2 = Potato()
    order_1 = Order()
    order_2 = Order()
    order_3 = Order()
    order_4 = Order()
    order_5 = Order()

    print(apple_1, " typ: ", type(apple_1))
    print(apple_2, " typ: ", type(apple_2))
    print(potato_1, " typ: ", type(potato_1))
    print(potato_2, " typ: ", type(potato_2))

    order_list = [Order(), Order(), Order(), Order(), Order()]
    product_dict = {"apple_1": Product(),
                    "apple_2": Product(),
                    "apple_3": Product(),
                    "apple_4": Product(),
                    }
    print(order_list)
    print(product_dict)
