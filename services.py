from validations import validate_positive_int, validate_not_empty
def add_product(inventory):
    product = validate_not_empty("Enter the name: "),
    price = float(validate_positive_int("Enter the price: ")),
    quantity = validate_positive_int("Enter the quantity: ")
    new_entry= {
        "product": product,
        "price": price,
        "quantity":quantity
    }
    inventory.append(new_entry)