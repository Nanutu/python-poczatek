# Utwórz dwa słowniki i połącz je w jeden wykorzystując operator **.
# Tak otrzymany słownik “rozpakuj” wywołując funkcję z zadania drugiego.

import random


def print_dict_elem(**kwargs):
    for first_name, age in kwargs.items():
        print(f"{first_name} = {age}")


def run_homework():
    dict_1 = {'val-0': 78, 'val-1': 64, 'val-2': 23, 'val-3': 51, 'val-4': 16}
    print(dict_1)
    dict_2 = {'val-a': 92, 'val-b': 2, 'val-c': 1, 'val-d': 95, 'val-e': 4}
    print(dict_2)
    dict_1_and_2 = {**dict_1, **dict_2}
    print(dict_1_and_2)

    print_dict_elem(**dict_1_and_2)


if __name__ == '__main__':
    run_homework()
