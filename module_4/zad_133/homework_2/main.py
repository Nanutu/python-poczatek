# Stwórz enuma reprezentującego kategorię produktu.
#
# Poszczególnym elementom nadaj odpowiednie nazwy (np. FOOD), zaś jako wartość podaj tekst,
# który ma być traktowany jako “wypisywalna” nazwa kategorii (np. “Jedzenie”).
#
# Zastąp nazwę kategorii w produkcie - kategorią (enumem).
#
# Dostosuj odpowiednio metodę generującą pozycje w zamówieniu i wypisującą produkt.

from shop.order import Order
from shop import data_generator


def run_homework():
    order_products = data_generator.generate_order_elements()
    order = Order("Mac", "XYZ", order_elements=order_products)
    print(order)


if __name__ == '__main__':
    run_homework()
