from validations import validate_positive_int, validate_positive_float_csv, validate_positive_int_csv, validate_not_empty_csv
from pathlib import Path
import csv
import os

base = Path(__file__).parent.parent
path = base / "data" / "inventory.csv"

# This creates a csv file with the actual inventory
def save_csv(inventory):
    '''
    This creates a csv file with the actual inventory
    '''
    if inventory == []:
        print("The inventory is empty")
    else:
        try:
            with open (path, "w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=["product", "unit_price", "quantity", "total_price"])
                writer.writeheader()
                for product in inventory:
                    writer.writerow({
                            "product" : product["product"],
                            "unit_price" : product["unit_price"],
                            "quantity" : product["quantity"],
                            "total_price" : product["total_price"]
                    })
            print(f'Inventory saved in path: {path}')

        # Management of exception errors while trying to write the csv file
        except PermissionError:
            os.system('cls')
            print("Error: You have no rights to write in this file or it is in usage")
            os.system('cls')
        except FileNotFoundError:
            os.system('cls')
            print("Error: The path does not exists")
        except OSError as e:
            os.system('cls')
            print(f'System error: {e}')
        except UnicodeDecodeError:
            os.system('cls')
            print("UniCodeDecodeError")
        except Exception as e:
            os.system('cls')
            print(f'Unexpected error: {e}')

# This upload a csv filo to the inventory of the program and uses validations for it to don't crash
def upload_csv(inventory):
            '''
            This upload a csv filo to the inventory of the program and uses validations for it to don't crash
            '''
            try:
                if inventory == []:
                    with open (path, "r", newline="", encoding="utf-8") as f:
                        reader = csv.DictReader(f)
                        if reader.fieldnames != ["product", "unit_price", "quantity", "total_price"]:
                            os.system('cls')
                            print("Invalid headers in the uploaded file")
                            return []
                        else:
                            inventory_uploaded = []
                            invalid_rows = 0
                            for row in reader:
                                local_dictionary = {}
                                try:
                                    local_dictionary["product"] = validate_not_empty_csv(row["product"])
                                    local_dictionary["unit_price"] = validate_positive_float_csv(row["unit_price"])
                                    local_dictionary["quantity"] = validate_positive_int_csv(row["quantity"])
                                    local_dictionary["total_price"] = validate_positive_float_csv(row["total_price"])
                                    inventory_uploaded.append(local_dictionary)
                                except ValueError:
                                    invalid_rows+=1
                            os.system('cls')        
                            print(f'CSV file uploaded with: {invalid_rows} invalid rows')
                            return inventory_uploaded
                else:
                    with open (path, "r", newline="", encoding="utf-8") as f:
                        reader = csv.DictReader(f)
                        if reader.fieldnames != ["product", "unit_price", "quantity", "total_price"]:
                            os.system('cls')
                            print("Invalid headers in the uploaded file")
                            return inventory
                        else:    
                            overwrite =validate_positive_int('''
    Enter: 
    "1" To overwirte your current inventory
    "2" To merge matching names updating price and adding the new quantity to the current one.
    Enter your answer here: ''', 2)
                            if overwrite == 1:
                                    inventory_uploaded = []
                                    invalid_rows = 0
                                    for row in reader:
                                        local_dictionary = {}
                                        try:
                                            local_dictionary["product"] = validate_not_empty_csv(row["product"])
                                            local_dictionary["unit_price"] = validate_positive_float_csv(row["unit_price"])
                                            local_dictionary["quantity"] = validate_positive_int_csv(row["quantity"])
                                            local_dictionary["total_price"] = validate_positive_float_csv(row["total_price"])
                                            inventory_uploaded.append(local_dictionary)
                                        except ValueError:
                                            invalid_rows+=1
                                    os.system('cls')
                                    print(f'CSV file uploaded with: {invalid_rows} invalid rows')
                                    return inventory_uploaded
                            else:
                                inventory_uploaded = []
                                invalid_rows = 0
                                for row in reader:
                                    for product in inventory:   
                                        local_dictionary = {}
                                        try:    
                                            row["product"] = validate_not_empty_csv(row["product"])                       
                                            if row["product"] == product["product"]:
                                                product["unit_price"] = validate_positive_float_csv(row["unit_price"])
                                                product["quantity"] = validate_positive_int_csv(row["quantity"]) + product["quantity"]
                                                product["total_price"] = validate_positive_float_csv(row["total_price"])
                                                inventory_uploaded.append(product)
                                            else:
                                                local_dictionary["product"] = validate_not_empty_csv(row["product"])
                                                local_dictionary["unit_price"] = validate_positive_float_csv(row["unit_price"])
                                                local_dictionary["quantity"] = validate_positive_int_csv(row["quantity"])
                                                local_dictionary["total_price"] = validate_positive_float_csv(row["total_price"])
                                                inventory_uploaded.append(local_dictionary)
                                        except ValueError:
                                            invalid_rows+=1
                                os.system('cls')
                                print(f'CSV file uploaded with: {invalid_rows} invalid rows')
                                return inventory_uploaded
            except PermissionError:
                os.system('cls')
                print("Error: You have no rights to read this file or it is in usage")
            except FileNotFoundError:
                os.system('cls')
                print("Error: The path does not exists")
            except OSError as e:
                os.system('cls')
                print(f'System error: {e}')
            except UnicodeDecodeError:
                os.system('cls')
                print("UniCodeDecodeError")
            except Exception as e:
                os.system('cls')
                print(f'Unexpected error: {e}')
                                                        
                    



        