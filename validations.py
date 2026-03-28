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

# This validates that a number is a positive float for csv services
def validate_positive_float_csv(number):
        try: 
            float_number = float(number)
            if float_number < 0:
                return ValueError
            else:
                 return float_number
        except ValueError:
            return ValueError

# This validates that a number is a positive int for csv services
def validate_positive_int_csv(number):
        try: 
            int_number = int(number)
            if int_number < 0:
                return ValueError
            else:
                return int_number
        except ValueError:
            return ValueError
        
def validate_not_empty_csv(text):
        if text == "":
             return ValueError
        else:
             return text