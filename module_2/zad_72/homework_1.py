# Napisz funkcję która przyjmie dowolną liczbę argumentów pozycyjnych i zwróci napis powstały z połączenia ich
# z wykorzystaniem myślnika jako łącznika pomiędzy poszczególnymi argumentami.


def inscription(*args):
    return "-".join(args)


def run_homework():
    counting = ["Raz", "dwa", "trzy", "cztery"]
    print(inscription(*counting))


if __name__ == '__main__':
    run_homework()