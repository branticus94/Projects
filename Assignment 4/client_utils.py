import time
from datetime import datetime

def get_integer_selection(prompt, min_value=None, max_value=None):
    while True:
        user_input = input(prompt)
        try:
            number = int(user_input)
            if (min_value is not None and number < min_value) or (max_value is not None and number > max_value):
                print(f"\nPlease enter a number between {min_value} and {max_value}.\n")
            else:
                return number
        except ValueError:
            print("\nInvalid input. Please enter a valid integer.\n")

def validate_user_selection(id_user_selection, iterable, iterable_name):
        while True:
            try:
                id_user_selection = int(id_user_selection)
            except ValueError:
                id_user_selection = input(f"\nThis is not a valid number, please insert a valid number for {iterable_name}.\n")
            for item in iterable:
                if item.get("id")== id_user_selection:
                    selected_item = item
                    return selected_item
            time.sleep(1)
            id_user_selection = input(f"\nThere is no available {iterable_name} with that id, please try again.\n")

def date_string_to_date_object(date_string):
    date_string = f"{date_string}"

    date_format = "%a, %d %b %Y %H:%M:%S GMT"

    date_object = datetime.strptime(date_string, date_format)

    return date_object
