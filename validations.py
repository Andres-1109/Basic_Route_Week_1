# This function validates that the result is a postive int and can evaluate a maximun range
def validate_positive_int(message, max_range=None):
    while True:
        try:
            result = int(input(message))
            if 1> result > max_range :
                print("Invalid answer")
            else:
                return result
        except ValueError:
            print("Invalid answer")
            
# This validates that the entry is not empty
def validate_not_empty(message):
    while True:
        try:
            concept = input(message)
            if concept != "":
                return concept
            else:
                print("Please write something")
        except ValueError:
            print("Please write something")