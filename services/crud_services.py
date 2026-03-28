from validations import validate_positive_int, validate_not_empty

# This add a product to the inventory list
def add_product(inventory):
    """
    This add a product to the inventory list
    """
    product = validate_not_empty("Enter the name of the product: ").lower()
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
    """"
    This shows the inventory
    """
    if inventory == []:
        print("The inventory is empty")
        return
    else:
        for i, product in enumerate(inventory, start=1):
            print(f"{i}. | Product: {product["product"]}| Total Price: {product["price"]}| Quantity: {product["quantity"]}|")

# This search a product by the name in the inventory
def search_product(inventory):
    """"
    This search a product by the name in the inventory
    """
    name = validate_not_empty("Enter the name of the product: ").lower()
    for product in inventory:
        index = 1
        if product["product"] == name:
            print(f"{index}. | Product: {product["product"]}| Total Price: {product["price"]}| Quantity: {product["quantity"]}|")
            index+=1
        else:
            print("Product not found")

# This updates a product in the inventory with new information
def update_product(inventory):
    """"
    This updates a product in the inventory with new information
    """
    show_inventory(inventory)
    number_of_products = len(inventory)
    choice = validate_positive_int("Enter the number of the product to delete: ", number_of_products) -1
    product_name = validate_not_empty("Enter the name of the product: ").lower()
    unit_price = float(validate_positive_int("Enter the unit price: "))
    quantity = validate_positive_int("Enter the quantity: ")
    total_price = unit_price * quantity

    inventory[choice]["product"] = product_name
    inventory[choice]["price"] = total_price
    inventory[choice]["quantity"] = quantity

# This deletes a selected product from the inventory
def delete_product(invetory):
    """"
    This deletes a selected product from the inventory
    """
    show_inventory(invetory)
    number_of_products = len(invetory)
    choice = validate_positive_int("Enter the number of the product to delete: ", number_of_products) -1
    invetory.pop(choice)

# This calculates total price and quantity of products in the whole inventory
def calculate_statistics(inventory):
    """"
    This calculates total price and quantity of products in the whole inventory
    """
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
    """"
    This finish the program
    """
    print("Thanks for using the service!")
    print("Closing the app...")
    return True
