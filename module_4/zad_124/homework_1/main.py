# Stwórz funkcję, która przyjmuje jako argument zbiór liczb, losuje liczbę od 0 do 10 i
# zwraca otrzymany wcześniej zbiór powiększony o wylosowaną liczbę.
#
# Wywołuj funkcję tak długo aż w wynikowym zbiorze znajdą się wszystkie liczby od 0 do 10.
#
# Za każdym razem jako argument przekaż do niej zwrócony przez wcześniejsze wywołanie zbiór.
#
# Zaimplementuj dwa warianty tej funkcji - działający z argumentem typu set oraz takim typu frozenset
# (w tym przypadku niezbędne będzie skorzystanie z metody union).
#
# Zastanów się, czy da się jedną implementacją obsłużyć obydwa przypadki? A co w sytuacji,
# gdybyś chciała/chciał zapamiętać wszystkie “pośrednie” zbiory, żeby na końcu wypisać jak wyglądały kolejne próby?

from shop.data_generator import generate_order_elements
from shop.discount_policy import PercentageDiscount, AbsoluteDiscount
from shop.order import Order
from shop.express_order import ExpressOrder
import random


def add_random_number_to_set(numbers):
    number = random.randint(0, 10)
    numbers.add(number)
    return numbers


def add_random_number_to_frozenset(numbers):
    number = random.randint(0, 10)
    return numbers.union({number})


def run_homework():
    # numbers = set()
    #
    # while len(numbers) < 11:
    #     print(numbers)
    #     add_random_number_to_set(numbers)
    # print(numbers)
    #
    numbers = frozenset()

    while len(numbers) < 11:
        print(numbers)
        numbers = add_random_number_to_frozenset(numbers)
    print(numbers)


if __name__ == '__main__':
    run_homework()
