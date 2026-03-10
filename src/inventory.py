print("Welcome!")
print("==========")
while True:
    try:
        productName = input(("Please insert the name of the product: "))
        if productName == "":
            print("Please insert a name")
        else:
            break
    except ValueError:
        print("Please insert a valid name")
while True:
    try:
        productPrice = float(input("Please insert the price of the product: "))
        if productPrice<= 0:
            print("Please insert a number above 0")
        else:
            break
    except ValueError:
        print("Please insert valid price")
while True:
    try:
        productQuantity = int(input("Please insert the quantity of the product: "))
        if productQuantity<= 0:
            print("Please insert an integer number above 0")
        else:
            break
    except ValueError:
        print("Please insert a valid quantity")
