from .products_store import products, update_products_quantity

orders = []



def new_order(product_name, product_quantity):
    price = products[product_name]["price"]
    available_quantity = products[product_name]["quantity"]
    if product_name not in products:
        print("Nie mamy tego towaru!")
    else:
        if product_quantity > available_quantity:
            print("Nie mamy tyle towaru!")
            return None
        else:
            total_price = price * product_quantity
            new_order = {
                "product": product_name,
                "quantity": product_quantity,
                "total price": total_price
            }
            update_products_quantity
            orders.append(new_order)
            return new_order





