def num_check(question):
    """Checks users enter an integer"""

    error = f"\nError, please enter an integer.\n"

    while True:

        try:
            response = int(input(question))

            return response

        except ValueError:
            print(error)
