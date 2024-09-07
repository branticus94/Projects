def get_integer(prompt, min_value=None, max_value=None):
    # Infinite loop to keep asking for input until valid
    while True:
        # Ask the user for input with the given prompt
        user_input = input(prompt)
        try:
            # Try to convert the input to an integer
            number = int(user_input)
            # Check if the number is within the specified range (if any)
            if (min_value is not None and number < min_value) or (max_value is not None and number > max_value):
                # If the number is out of bounds, display an error message
                print(f"\nPlease enter a number between {min_value} and {max_value}.\n")
            else:
                # If valid, return the number
                return number
        except ValueError:
            # If the input is not a valid integer, display an error message
            print("\nInvalid input. Please enter a valid integer.\n")


def get_yes_no(prompt):
    # Infinite loop to keep asking for input until valid
    while True:
        # Get input from the user, remove extra spaces, and convert to lowercase
        user_input = input(prompt).strip().lower()

        # If the input is 'y' (yes) or 'n' (no), return it
        if user_input in ['y', 'n']:
            return user_input
        else:
            # If invalid, show an error message and ask again
            print("Invalid input. Please enter 'y' for yes or 'n' for no.")