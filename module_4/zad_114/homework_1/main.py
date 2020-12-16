# Używając list comprehensions wygeneruj listy zawierające liczby od 1 do 30 podzielne kolejno przez 3 oraz przez 5.
#
# To znaczy, że na pierwszej liście powinny znaleźć się liczby od 1 do 30 podzielne przez 3,
# a na drugiej liście liczby od 1 do 30 podzielne przez 5.
#
# Następnie, połącz obie listy w jedną i wypisz wynik.

import random
import math


def run_homework():
    list_1 = [number for number in range(1, 31) if number % 3 == 0]
    print(list_1)
    list_2 = [number for number in range(1, 31) if number % 5 == 0]
    print(list_2)

    list_3 = list_1 + list_2
    print(list_3)


if __name__ == '__main__':
    run_homework()
