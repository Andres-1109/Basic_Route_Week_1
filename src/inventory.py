    #Imports os library to later use it on clearing the terminal
import os
    #Prints a message that welcomes the customer
print("Welcome!")
print("==========")
    #Asks the name to the user and validates that the name received is not empty
while True:
        productName = input(("Please insert the name of the product: "))
        if productName == "":
            print("Please insert a name")
        else:
            break
    #Asks the price and validates that it is a float above 0
while True:
    try:
        productPrice = float(input("Please insert the price of the product: "))
        if productPrice<= 0:
            print("Please insert a number above 0")
        else:
            break
    except ValueError:
        print("Please insert valid price")
    #Asks the quantity and validates that it is an integer above 0
while True:
    try:
        productQuantity = int(input("Please insert the quantity of the product: "))
        if productQuantity<= 0:
            print("Please insert an integer number above 0")
        else:
            break
    except ValueError:
        print("Please insert a valid quantity")
    #Calculates the total cost of the product by multiplying the price by the quantity
totalCost = productPrice * productQuantity
    #Clear the terminal to print the final message
os.system("cls")
    #Prints a message with the variables received and the total cost calculated
print (f"Your product is |{productName}|, the price is |${productPrice}|, the quantity is |{productQuantity}| and the total cost is |${totalCost}|")
print("==========")
print("Thanks for using our services!")

"""
    - Program explanation

1) The program works to ask the customer for product's name, price and quantity. 
2) While doing this, the program validates each input to guarantee that it complies with the requirements.
3) After this, the program calculates the total cost of the product multiplying price by quantity.
4) The program prints a message with the variables received and the total cost of the product calculated.

"""