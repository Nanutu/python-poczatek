# Napisz funkcję, która przyjmie dowolną liczbę argumentów nazwanych i wypisze sposób w jaki została wywołana,
# tzn. poszczególne nazwy argumentów, znak równa się i wartość (np. first_name=Mikołaj, age=134).


def print_dict_elem(**kwargs):
    for first_name, age in kwargs.items():
        print(f"{first_name} = {age}")


def run_homework():
    counting = {"Maciej": 27, "Dorota": 27, "Seba": 29, "Zosia": 2}
    print_dict_elem(**counting)
    print("ZMIANA!")
    print_dict_elem(Maciej=22, Dorcia=21)


if __name__ == '__main__':
    run_homework()