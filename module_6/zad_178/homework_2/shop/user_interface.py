from shop.errors import TemporaryOutOfStock, ProductNotAvailable, NotValidInput
from shop.order import Order
from shop.store import Store
from shop.persistence import save_order, load_orders
from enum import Enum


class Action(Enum):
    NEW_ORDER = "1"
    HISTORY = "2"


def handle_customer():
    say_hello()
    selected_action = select_action()
    if selected_action is Action.NEW_ORDER:
        order = init_order()
        while want_more_products():
            add_product_to_order(order, Store.AVAILABLE_PRODUCTS)
        print_order_summary(order)
        save_order(order)
    else:
        show_history()


def say_hello():
    print("Witaj w naszym sklepie!")


def select_action():
    selected_action = input("Chcesz złożyć nowe zamówienie (1) czy zobaczyć historię swoich zamówień (2)?")
    try:
        return Action(selected_action)
    except ValueError:
        print("Możliwe są tylko dwie opcje - domyślnie wybieramy nowe zamówienie ;)")
        return Action.NEW_ORDER


def show_history():
    orders = load_orders()
    print("Lista zamówień:")
    print(orders)


def init_order():
    first_name = input("Podaj swoje imię.")
    last_name = input("Podaj swoje nazwisko.")
    return Order(first_name, last_name)
    # TODO: Pobierz imię i nazwisko i zwróć to czego oczekuje wołający w handle customer


def want_more_products():
    selection = input("Czy chcesz dodać produkty do zamówienia? T/N: ")
    if selection.upper() != "T" and selection.upper() != "N":
        print("Opcje są tylko dwie - zakładam, że chcesz coś zamówić ;)")
        return True
    return selection.upper() == "T"


def want_see_orders():
    selection = input("Czy chcesz zobaczyć złożone zamówienia? T/N: ")
    if selection.upper() != "T" and selection.upper() != "N":
        print("Opcje są tylko dwie - zakładam, że chcesz je zobaczyć ;)")
        return True
    return selection.upper() == "T"


def add_product_to_order(order, available_products):
    print("Oto dostępne produkty:")
    for index, available_product in enumerate(available_products):
        print(f"{index}) {available_product.product}")

    try:
        product_index_str = input("Wybierz numer: ")
        product_index = parse_product_index(product_index_str, max_index=len(available_products) - 1)

        quantity_str = input("Podaj liczbę sztuk: ")
        quantity = parse_quantity(quantity_str)
    except NotValidInput as input_error:
        print(f"{input_error} - podałeś błędne dane.")
        return
        # TODO: Obsłuż błędne dane podane przez użytkownika

    try:
        order.add_product_to_order(available_products[product_index].product, quantity)
    except TemporaryOutOfStock as error:
        print(f"Niestety mamy dostępne tylko {error.available_quantity} sztuk produktu {error.product_name}")
    except ProductNotAvailable as error:
        print(f"Produkt {error.product_name} nie jest dostępny. Wybierz inny.")


def parse_product_index(product_index_str, max_index):
    try:
        product_index = int(product_index_str)
    except ValueError:
        raise NotValidInput(f"Numer produktu musi być liczbą.")

    if not 0 <= product_index <= max_index:
        raise NotValidInput(f"Numer produktu musi mieścić się w przedziale 0-{max_index}.")

    return product_index
    # TODO: Zamień napis na liczbę i upewnij się, że jest poprawna (czyli, że na pewno taki indeks będzie na liście)
    # TODO: W przypadku błędu rzuć odpowiedni wyjątek, który oczekiwany jest w metodzie "wyżej"


def parse_quantity(quantity_str):
    try:
        quantity = int(quantity_str)
    except ValueError:
        raise NotValidInput(f"Ilość produktu musi być liczbą.")
    if not quantity > 0:
        raise NotValidInput(f"Ilość produktu musi być większa od 0.")
    return quantity
    # TODO: Zamień napis na liczbę i upewnij się, że jest większa od 0, w razie czego rzuć odpowiedni wyjątek


def print_order_summary(order):
    print("Twoje zamówienie to:")
    print(order)
    print("Dziękujemy i zapraszamy ponownie!")
