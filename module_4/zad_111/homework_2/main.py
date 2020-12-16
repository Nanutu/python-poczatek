# Napisz funkcję generującą losowy identyfikator. Identyfikator powinien być w formacie 00001,
# tzn. zawsze o długości pięciu znaków, dopełniony z lewej strony odpowiednią liczbą zer.


import random
import math


def run_homework():
    base = random.randint(1, 9999)
    print(str(base).zfill(5))


if __name__ == '__main__':
    run_homework()
