# Wygeneruj dwie listy zawierające losowe liczby całkowite i połącz je w jedną wykorzystując operator *.
import random


def make_random_list(list_length):
    random_int_list = []
    for i in range(list_length):
        random_int_list.append(random.randint(1, 100))
    return random_int_list


def run_homework():
    random_int_list_1 = make_random_list(5)
    random_int_list_2 = make_random_list(5)

    print(random_int_list_1)
    print(random_int_list_2)

    list_1_and_list_2 = [*random_int_list_1, *random_int_list_2]

    print(list_1_and_list_2)


if __name__ == '__main__':
    run_homework()
