# Zmodyfikuj rozwiązanie zadania pierwszego, tak aby do wypisywania wykorzystać metodę format.

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
    print(f"Nazywasz się {clear_name} {clear_surname} - jak miło Cię poznać :)".format(clear_name=clear_name, clear_surname=clear_surname))




if __name__ == '__main__':
    run_homework()
