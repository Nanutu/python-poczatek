# Wylosuj 6 liczb typu float z przedziału od -20 do 20 oraz 3 liczby całkowite z przedziału od 1 do 10.
#
# Następnie na pierwszych trzech liczbach typu float zastosuj zaokrąglanie (kolejno round, ceil oraz floor).
#
# Kolejne trzy liczby typu float podnieś do potęgi o wartości odpowiednio pierwszej, drugiej i trzeciej wylosowanej liczby całkowitej.


import random
import math


def run_homework():
    float_numbers = []
    for i in range(0, 6):
        float_numbers.append(random.uniform(-20, 20))
    print(float_numbers)

    int_numbers = []
    for i in range(0, 3):
        int_numbers.append(random.randint(1, 10))
    print(int_numbers)

    for i in range(0, 3):
        print(float_numbers[i])
        print(round(float_numbers[i]))
        print(math.ceil(float_numbers[i]))
        print(math.floor(float_numbers[i]))
        print("-----------------")

    for i in range(3, 6):
        print(float_numbers[i])
        print(int_numbers[i-3])
        print(float_numbers[i]**int_numbers[i-3])
        print("++++++++++++++++++")


if __name__ == '__main__':
    run_homework()
