# Zrefaktoryzuj rozwiązanie zadania drugiego z lekcji funkcja jako obiekt z modułu Programowanie Obiektowe I.
# Jest to zadanie, w którym dodawaliśmy polityki rabatowe.**
#
#-Utwórz nowy moduł data_generator i przenieś do niego z pliku main funkcję generującą elementy zamówienia.
#
#-Ulepsz tę funkcję dodając do niej parametr liczby produktów w zamówieniu z domyślną wartością None
#(jeżeli nie przekazano oczekiwanej liczby produktów to wylosuj ją z zakresu od 1 do maksymalnej liczby pozycji w zamówieniu).
#
#-Zastąp graniczne wartości, z których generowana jest liczba produktów w pozycji zamówienia oraz cena jednostkowa produktu stałymi,
#czyli zapisanymi według odpowiedniej konwencji zmiennymi globalnymi na poziomie nowo utworzonego modułu data_generator.
#
#-Usuń nieużywaną metodę klasy Order: generate_order.


from shop.order import Order
from shop.discount_policy import loyal_customer_policy, christmas_policy
from shop.data_generator import generate_order


def run_homework():
    order_elements = generate_order(5)
    normal_order = Order(client_first_name="Maciej", client_last_name="Xyz", order_elements=order_elements)
    loyal_customer_order = Order(client_first_name="Maciej", client_last_name="Xyz", order_elements=order_elements,
                                 discount_policy=loyal_customer_policy)
    christmas_order = Order(client_first_name="Maciej", client_last_name="Xyz", order_elements=order_elements,
                            discount_policy=christmas_policy)

    print(normal_order)
    print(loyal_customer_order)
    print(christmas_order)


if __name__ == '__main__':
    run_homework()
