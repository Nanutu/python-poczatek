# Napisz funkcję, która wczyta od użytkownika jej/jego imię i nazwisko,
# “wyczyści je” z białych znaków na początku i końcu tekstu, a następnie wypisze jakieś zdanie z tymi danymi
# np. “Nazywasz się {first_name} {last_name} - jak miło Cię poznać :)”

import random
import math


def run_homework():
    name = input("Podaj swoje imię.")
    surname = input("Podaj swoje nazwisko.")
    name = name.strip()
    surname = surname.strip()
    print(f"“Nazywasz się {name} {surname} - jak miło Cię poznać :)”")


if __name__ == '__main__':
    run_homework()
