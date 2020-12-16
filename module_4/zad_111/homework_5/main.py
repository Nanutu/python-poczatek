# Zmodyfikuj rozwiązanie zadania pierwszego, tak aby do wypisywania wykorzystać formatowanie z procentem.

# Napisz funkcję, która wczyta od użytkownika jej/jego imię i nazwisko,
# “wyczyści je” z białych znaków na początku i końcu tekstu, a następnie wypisze jakieś zdanie z tymi danymi
# np. “Nazywasz się {first_name} {last_name} - jak miło Cię poznać :)”

import random
import math


def run_homework():
    name = input("Podaj swoje imię.")
    surname = input("Podaj swoje nazwisko.")
    clear_name = name.strip()
    clear_surname = surname.strip()
    print("Nazywasz się %(clear_name)s %(clear_surname)s - jak miło Cię poznać :)" % {"clear_name": clear_name, "clear_surname": clear_surname})


if __name__ == '__main__':
    run_homework()
