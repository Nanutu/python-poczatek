# Wczytaj od użytkownika listę ulubionych sportów, a następnie stosując slicing wypisz co drugi,
# pomijając pierwszy sport z listy.


import random
import math


def run_homework():
    list_of_sports = input("Podaj listę ulubionych sportów. ")
    print(list_of_sports[1::2])


if __name__ == '__main__':
    run_homework()
