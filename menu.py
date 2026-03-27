from data.menu_options import get_options
from validations import validate_positive_int

def menu(inventory):
    while True:    
        options = get_options()
        number_of_options = len(options)
        for i, option in enumerate(options, start=1):
            print(f"{i}. {option["option"]}")
        
        choice = validate_positive_int("Select an option: ", number_of_options) -1
        result = options[choice]["action"](inventory)
        if result:
            break

