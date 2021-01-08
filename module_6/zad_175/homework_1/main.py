# W skrypcie main złap wyjątek rzucany przy przekroczeniu limitu zamówienia
# i wypisz prosty komunikat.

# Rozbuduj poprzednie rozwiązanie o wypisanie informacji zawartych w obiekcie wyjątku.


from shop.order import Order
from shop import data_generator
from shop.errors import OrderElementsLimitError


def ask_for_name():
    name = input("Podaj trzy pierwsze litery imienia.")
    name_len = len(name)

    if name_len > 3:
        raise ValueError("Za długie!")
    if name_len < 3:
        raise ValueError("Za krótkie!")

    print("Dziękuję:)")


def run_example():
    try:
        ask_for_name()
    except ValueError as error:
        print(f"Podano złą ilość liter! - {error}.")
    else:
        print("Wszystko w porządku, dziękuję.")
    finally:
        print("FINITO!")


if __name__ == "__main__":
    run_example()
