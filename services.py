from validations import validate_positive_int, validate_not_empty

# This add a product to the inventory list
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

# This shows the inventory
def show_inventory(inventory):
    if inventory == []:
        print("The inventory is empty")
        return
    else:
        for i, product in enumerate(inventory, start=1):
            print(f"{i}. | Product: {product["product"]}| Total Price: {product["price"]}| Quantity: {product["quantity"]}|")

# This calculates total price and quantity of products in the whole inventory
def calculate_statistics(inventory):
    if inventory == []:
        return print("The inventory is empty")
    else: 
        total_inventory_price = 0
        total_products_quantity = 0
        for product in inventory:
            total_inventory_price = total_inventory_price + product["price"]
            total_products_quantity = total_products_quantity + product["quantity"]
        print(f"The total price of the inventory is: ${total_inventory_price}")
        print(f"The total quantity of products is: {total_products_quantity}")

# This finish the program
def exit_program(inventory):
    print("Thanks for using the service!")
    print("Closing the app...")
    return True