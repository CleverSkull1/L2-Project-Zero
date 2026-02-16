def num_check(question, num_type, exit_code="exit8"):
    """Checks users enter an integer / float that is more than
    zero (or the exit code)"""

    if num_type== "integer":
        error = "Error, please enter an integer greater than 0."
        change_to = int
    else:
        error = "Error, please enter a number greater than 0."
        change_to = float

    while True:
        response = input(question).lower()

        if response == exit_code:
            return response
        try:
            response = change_to(response)

            if response > 0:
                return response
            else:
                print(f"\n{error}\n")
        except ValueError:
            print(f"\n{error}\n")

while True:
    print()

    my_float = num_check("Please enter a number more than 0: ", "float")
    print()
    my_int = num_check("Please enter an integer more than 0: ", "integer")
