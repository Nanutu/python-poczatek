from shop.orders import new_order


def run_shop():
    print("Witaj w naszym sklepie!")
    product_name = input("Jaki towar chcesz kupić?")
    product_quantity = int(input("Ile tego towaru chcesz kupić?"))

    result = new_order(product_name, product_quantity)
    if result is not None:
        total_price = result["total price"]
        print(f"Łączny koszt zakupów to {total_price}zł.")


if __name__ == "__main__":
    run_shop()
