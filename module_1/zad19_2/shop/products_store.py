products = {
    "bread": {
        "quantity": 3,
        "price": 5
    },
    "eggs": {
        "quantity": 10,
        "price": 1
    },
    "flour": {
        "quantity": 8,
        "price": 2
    }
}


def update_products_quantity(product_name, product_quantity):
    products[product_name]["quantity"] -= product_quantity

