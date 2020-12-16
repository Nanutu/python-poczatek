# Stwórz klasę reprezentującą produkt z terminem ważności (dziedziczącą po klasie Product).
#
# Rozszerz implementację bazową o dodatkowe pola: rok produkcji oraz liczbę lat ważności i metodę does_expire.
#
# Metoda ta przyjmuje jako argument aktualny rok oraz sprawdza czy od daty produkcji do podanego roku
# minęła liczba lat większa od tej podanej jako lata ważności.


from shop.product import  ExpiringProduct


def run_homework():
    bbd_product = ExpiringProduct(
        name="Corn",
        category_name="Food",
        unit_price=10,
        production_year=2015,
        validity_years=4
    )
    print(bbd_product.does_expire(2016))
    print(bbd_product.does_expire(2022))


if __name__ == '__main__':
    run_homework()
