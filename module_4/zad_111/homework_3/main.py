# Wczytaj od użytkownika jej/jego ulubione kolory (jako jeden napis, np. rozdzielony przecinkiem).
#
# Sprawdź, czy znajduje się wśród nich niebieski, a następnie wypisz odpowiedni komunikat.


import random
import math


def run_homework():
    colors = input("Wypisz po przecinku swoje ulubione kolory.")
    if colors.lower().find("niebieski") != -1:
        print("Jest.")
    else:
        print("Nima.")

    if "niebieski" in colors.lower():
        print("Jest.")
    else:
        print("Nima.")


if __name__ == '__main__':
    run_homework()
