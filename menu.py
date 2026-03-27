from data.menu_options import get_options
from validations import validate_positive_int

def menu(inventory):
    while True:    
        options = get_options()
        number_of_options = len(options)
        # This shows the options of the menu
        for i, option in enumerate(options, start=1):
            print(f"{i}. {option["option"]}")
        
        # This ask for the option to access from the menu
        choice = validate_positive_int("Select an option: ", number_of_options) -1

        # This executes the function that is contained on the option's dictionary
        result = options[choice]["action"](inventory)

        # This helps exit the program with the exit function that returns true
        if result:
            break

