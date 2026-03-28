from services.crud_services import add_product, show_inventory, calculate_statistics, exit_program, search_product, update_product, delete_product

# This create the options that will appear in the menu
def get_options():
    return [
        {"option":"Add product", "action": add_product},
        {"option":"Show inventory", "action": show_inventory},
        {"option":"Search product","action":search_product},
        {"option":"Update product","action":update_product},
        {"option":"Delete product","action":delete_product},
        {"option":"Calculate statistics", "action":calculate_statistics},
        {"option":"Exit","action":exit_program}
    ]