from validations import validate_positive_int, validate_not_empty
def add_product(inventory):
    product = validate_not_empty("Enter the name: ")
    unit_price = float(validate_positive_int("Enter the unit price: "))
    quantity = validate_positive_int("Enter the quantity: ")
    total_price = unit_price * quantity
    new_entry= {
        "product": product,
        "price": total_price,
        "quantity":quantity
    }
    inventory.append(new_entry)

def show_inventory(inventory):
    if inventory == []:
        return print("The inventory is empty")
    else:
        for i, product in enumerate(inventory, start=1):
            print(f"{i}. | Product: {product["product"]}| Total Price: {product["price"]}| Quantity: {product["quantity"]}|")