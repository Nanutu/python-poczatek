# Napisz test sprawdzający poprawność wykonanej w poprzednim module metody magicznej __eq__
# w klasie Product - czyli porównywania produktów.
#
# Dla przypomnienia, dwa produkty są sobie równe, gdy mają taką samą nazwę, taką samą kategorię
# i taką samą cenę jednostkową.
#
# Wykorzystaj tuple do przygotowania różnych zestawów parametrów danych do algorytmu testującego.


from shop.product import Product
import random


def test_product_eq():
    parameters = [
        ("Banan", "Owoc", 2, "Ananas", "Owoc", 4, False),
        ("Stek", "Mięso", 50, "Yaris", "Auto", 10000, False),
        ("Yaris", "Auto", 10000, "Yaris", "Auto", 10000, True),
        ("Banan", "Owoc", 2, "Ananas", "Owoc", 4, True)
    ]

    for params in parameters:
        name, category_name, unit_price, other_name, other_category_name, other_unit_price, expected_result = params
        result = Product(name, category_name, unit_price, Product.identifier) == \
                 Product(other_name, other_category_name, other_unit_price, Product.identifier)
        if result == expected_result:
            print("Super!")
        else:
            print(f"Błąd! Dla danych {params} wynik powinen wynosić {expected_result} a wynosi {result}.")


def run_homework():
    test_product_eq()


if __name__ == '__main__':
    run_homework()
