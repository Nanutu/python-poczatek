# Wygeneruj 5 losowych zamówień i posortuj je rosnąco po ich łącznej cenie.
#
# Zastosuj własną funkcję zwracającą odpowiednią wartość, która będzie używana do porównania przez funkcję sortującą.
#
# Zmodyfikuj rozwiązanie zadania zamieniając funkcję wykorzystywaną przez metodę sortującą na lambdę.


from shop.order import Order


def run_homework():

    orders = []
    for i in range(5):
        orders.append(Order.generate_order())

    orders.sort(key=lambda order: order.total_price)
    for order in orders:
        print(order)


if __name__ == '__main__':
    run_homework()
