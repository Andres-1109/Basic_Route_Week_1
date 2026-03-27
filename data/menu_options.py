from services import add_product, show_inventory
def get_options():
    return [
        {"option":"Add product", "action": add_product},
        {"option":"Show inventory", "action": show_inventory},
        {"option":"Calculate statistics", "action":"calculate_statistics"},
        {"option":"Exit","action":"exit"}
    ]