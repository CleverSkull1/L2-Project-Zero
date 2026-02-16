def int_check(question, low, high):
    """Checks users enter an integer between two values"""
    error = f"Please enter an integer between {low} and {high}."
    while True:
        try:
            response = int(input(question))

            if low <= response <= high:
                return response
            else:
                print(error)
        except ValueError:
            print(error)