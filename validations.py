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