# Klasy Apple oraz Potato są prostymi pojemnikami na dane.
#
# Zastąp ich dotychczasowe implementacje wariantem dataclass.


from shop.apple import Apple
from shop.potato import Potato


def run_homework():
    green_apple = Apple(species_name="Green", size="M", price=3.5)
    red_apple = Apple(species_name="Red", size="S", price=2.8)

    print(green_apple.species_name, green_apple)
    print(f"10kg zielonego jabłka kosztuje: {green_apple.calculate_price(10)}")
    print(red_apple.species_name, red_apple)
    print(f"5kg czerwonego jabłka kosztuje: {red_apple.calculate_price(5)}")

    old_potato = Potato(species_name="Potato Old", size="S", price=1.55)
    print(f"8kg starych ziemniaków kosztuje: {old_potato.calculate_price(8)}")
    print(old_potato.species_name, old_potato)


if __name__ == '__main__':
    run_homework()
