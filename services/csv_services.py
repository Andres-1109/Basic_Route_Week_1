from pathlib import Path
import csv

base = Path(__file__).parent.parent
path = base / "data" / "inventory.csv"

def save_csv(inventory):
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

        except PermissionError:
            print("Error: You have no rights to write in this file or it is in usage")
        except FileNotFoundError:
            print("Error: The path does not exists")
        except OSError as e:
            print(f'System error: {e}')
        except Exception as e:
            print(f'Unexpected error: {e}')
