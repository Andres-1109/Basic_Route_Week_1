def validate_positive_int(message, max_range):
    while True:
        try:
            result = int(input(message))
            if 1> result > max_range :
                print("Invalid answer")
            else:
                return result
        except ValueError:
            print("Invalid answer")