# Utwórz klasę TaxCalculator z metodą statyczną obliczającą wartość podatku dla danej pozycji z zamówieniu
# (procent przemnożony przez wartość pozycji).
#
# Przyjmij następujące stawki podatkowe - w zależności od nazwy kategorii, do której należy produkt:
#
#     a) 5% - “Owoce i warzywa”
#     b) 8% - “Jedzenie”
#     c) 20% - Wszystkie pozostałe kategorie


from shop.order import Order
from shop.order_element import OrderElement
from shop.product import Product
from shop.tax_calculator import TaxCalculator


def run_homework():
    cookies = Product(name="Cookies", category_name="Food", unit_price=5)
    apples = Product(name="Apples", category_name="fruits and vegetables", unit_price=5)
    other = Product(name="other", category_name="other", unit_price=5)

    ten_cookies = OrderElement(product=cookies, quantity=10)
    five_apples = OrderElement(product=apples, quantity=5)
    three_other = OrderElement(product=other, quantity=3)

    tax_cookies = TaxCalculator.tax_for_order_element(ten_cookies)
    tax_apples = TaxCalculator.tax_for_order_element(five_apples)
    tax_other = TaxCalculator.tax_for_order_element(three_other)

    print(f"Price for {ten_cookies.product.name} = {ten_cookies.calculate_price()} + {tax_cookies:.2f}.")
    print(f"Price for {five_apples.product.name} = {five_apples.calculate_price()} + {tax_apples:.2f}.")
    print(f"Price for {three_other.product.name} = {three_other.calculate_price()} + {tax_other:.2f}.")


if __name__ == '__main__':
    run_homework()
