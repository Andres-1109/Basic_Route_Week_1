from validations import validate_positive_int, validate_not_empty
import os

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
        "unit_price": unit_price,
        "quantity":quantity,
        "total_price": total_price
    }
    inventory.append(new_entry)
    os.system('cls')
    return inventory

# This shows the inventory
def show_inventory(inventory):
    """"
    This shows the inventory
    """
    if inventory == []:
        print("The inventory is empty")
        os.system('cls')
        return inventory
    else:
        for i, product in enumerate(inventory, start=1):
            print(f'{i}. | Product: {product["product"]}| Unit Price: {product["unit_price"]}| Quantity: {product["quantity"]}| Total Price: {product["total_price"]}')
        os.system('cls')
        return inventory

# This search a product by the name in the inventory
def search_product(inventory):
    """"
    This search a product by the name in the inventory
    """
    name = validate_not_empty("Enter the name of the product: ").lower()
    for product in inventory:
        index = 1
        if product["product"] == name:
            print(f'{index}. | Product: {product["product"]}| Unit Price: {product["unit_price"]}| Quantity: {product["quantity"]}| Total Price: {product["total_price"]}')
            index+=1
        else:
            pass
    if index == 1:
        print("Product nor found")
    os.system('cls')
    return inventory

# This updates a product in the inventory with new information
def update_product(inventory):
    """"
    This updates a product in the inventory with new information
    """
    show_inventory(inventory)
    number_of_products = len(inventory)
    choice = validate_positive_int("Enter the number of the product to update: ", number_of_products) -1
    product_name = validate_not_empty("Enter the name of the product: ").lower()
    unit_price = float(validate_positive_int("Enter the unit price: "))
    quantity = validate_positive_int("Enter the quantity: ")
    total_price = unit_price * quantity

    inventory[choice]["product"] = product_name
    inventory[choice]["unit_price"] = unit_price
    inventory[choice]["quantity"] = quantity
    inventory[choice]["total_price"] = total_price
    os.system('cls')
    return inventory

# This deletes a selected product from the inventory
def delete_product(inventory):
    """"
    This deletes a selected product from the inventory
    """
    show_inventory(inventory)
    number_of_products = len(inventory)
    choice = validate_positive_int("Enter the number of the product to delete: ", number_of_products) -1
    inventory.pop(choice)
    os.system('cls')
    return inventory

# This calculates total price and quantity of products in the whole inventory and shows most expensive and quantity product
def calculate_statistics(inventory):
    """"
    This calculates total price and quantity of products in the whole inventory and shows most expensive and quantity product
    """
    if inventory == []:
        return print("The inventory is empty")
    else: 
        total_inventory_price = 0
        total_products_quantity = 0
        most_expensive_product = {"total_price": 0}
        most_quantity_product = {"quantity": 0}
        for product in inventory:
            total_inventory_price = total_inventory_price + product["total_price"]
            total_products_quantity = total_products_quantity + product["quantity"]
            if most_expensive_product["total_price"] < product["total_price"]:
                most_expensive_product = product
            if most_quantity_product["quantity"] < product["quantity"]:
                most_quantity_product = product
        print(f'''
The total price of the inventory is: ${total_inventory_price}
The total quantity of products is: {total_products_quantity}
The most expensive product is {most_expensive_product["product"]}, total price ${most_expensive_product["total_price"]}  
The product with more quantity is {most_quantity_product["product"]}, quantity {most_quantity_product["quantity"]}''')
        os.system('cls')
        return inventory


# This finish the program
def exit_program(inventory):
    """"
    This finish the program
    """
    os.system('cls')
    print("Thanks for using the service!")
    print("Closing the app...")
    return "exit"
