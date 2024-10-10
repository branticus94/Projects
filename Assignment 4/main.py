from datetime import datetime

from client_fetch_data_helpers import get_all_libraries, get_available_books, get_all_books, get_book_availability, \
    get_book_information, get_all_customers, get_outstanding_loans, get_overdue_books, put_return_book, \
    put_update_customer, post_add_book, post_add_customer, delete_delete_book, post_checkout_book, get_index
from client_utils import get_integer_selection, validate_user_selection, date_string_to_date_object
import pyfiglet
import time
import re

def check_server_running():
    try:
        get_index()['message']
    except TypeError:
        print("\nThe server is not running.\n\nPlease start the server and re-try the application.\n\nExiting application:")
        exit_application()

# Functions which print menu/welcome to the console
def print_welcome():
    logo_text = "Warwickshire\n          Libraries"

    ascii_art = pyfiglet.figlet_format(logo_text)

    print(ascii_art)

    time.sleep(1)

    print(r'                     ______ ______')
    print(r'                   _/      Y      \_')
    print(r'                  // ~~ ~~ | ~~ ~  \\')
    print(r'                 // ~ ~ ~~ | ~~~ ~~ \\')
    print(r'                //________.|.________\\')
    print(r"               `----------`-'----------'")

    time.sleep(1)

def print_menu():
    print("\nWelcome to Warwickshire libraries. Please select an option from the following menu:")

    time.sleep(1)

    for option in menu_options:
        print(f"{option["id"]}. {option["menu option"]}")

def print_admin_menu ():
    print("\nWelcome to library admin. Please select an option from the following menu:")

    time.sleep(1)

    for option in admin_menu_options:
        print(f"{option["id"]}. {option["menu option"]}")

# Functions which allow for user to select from a menu
def menu_selector(admin_menu=False):
    if not admin_menu:
        menu_choice = get_integer_selection("\nPlease select an option: \n", 1, len(menu_options))
        for option in menu_options:
            if option["id"] == menu_choice:
                menu_function = option["function"]
                menu_function()
    else:
        menu_choice = get_integer_selection("\nPlease select an option: \n", 1, len(admin_menu_options))
        for option in admin_menu_options:
            if option["id"] == menu_choice:
                menu_function = option["function"]
                menu_function()

def admin_actions ():
    print_admin_menu()
    menu_selector(admin_menu=True)

def exit_application ():
    print("\nThank you for using Warwickshire library services.\n\nRemember: the only thing that you absolutely have to know is the location of the library \n— Albert Einstein!")
    exit()

def return_to_menu ():
    while True:
        response = input(f"\nWould you like to return to the main menu? (y/n): \n").strip().lower()
        if response == 'y':
            start_menu()
        elif response == 'n':
            print("\nThank you for using Warwickshire library services.\n\nRemember: the only thing that you absolutely have to know is the location of the library \n— Albert Einstein!")
            exit()
        else:
            print("Invalid input. Please enter 'y' for yes or 'n' for no.")

# Functions for the main customer menu
def library_locations():

    libraries = get_all_libraries()

    if libraries == "No available libraries":
        print("\nWe are unable to retrieve libraries data at this time returning to main menu.\n")
        time.sleep(1)
        return start_menu()
    else:
        print("\nHere is a list of libraries in Warwickshire:\n")
        time.sleep(1)

        for library in libraries:
            for key in library:
                if key == "id":
                    pass
                else:
                    print(f'{key.capitalize().replace('_',' ')}: {library[key]}')
            time.sleep(1)
            print()

    return_to_menu()

def available_books ():
    try:
        time.sleep(1)

        libraries = get_all_libraries()

        if libraries == "No available libraries":
            print("\nWe are unable to retrieve libraries data at this time. Returning to main menu.\n")
            time.sleep(1)
            return start_menu()
        else:
            print("\nPlease select a library to view library catalogue:\n")
            for library in libraries:
                print(f"Library id: {library["id"]}, Library name: {library['location']}")
            time.sleep(1)
            library_id_selection = input("\nPlease type in your chosen library id to see available books:\n")
            library = validate_user_selection(id_user_selection = library_id_selection, iterable = libraries, iterable_name= "library")
            selected_library_id, selected_library_location = library['id'], library['location']

            books = get_available_books(selected_library_id)
            if books == "No available books":
                print("\nWe are unable to retrieve books information at this time returning to main menu.\n")
                return start_menu()
            print(f"\nThe catalogue for {selected_library_location} includes:\n")
            time.sleep(1)
            for i, book in enumerate(books):
                print(f"{i+1}. {book['title']} by {book['author_name']}\n   Inventory: {book['inventory']}")
    except Exception as e:
        print(e)

    return_to_menu()

def book_availability ():
    try:
        time.sleep(1)

        books = get_all_books()

        if books == "No available books":
            print("\nWe are unable to retrieve books data at this time. Returning to main menu.\n")
            time.sleep(1)
            return start_menu()
        else:
            print("\nPlease select a book to view availability:\n")

            time.sleep(1)

            for book in books:
                print(f"Book id: {book['id']}, Book name: {book['title']}")

            time.sleep(1)

            book_id_selection = input("\nPlease type in your chosen book id to see availability.\n")

            selected_book = validate_user_selection(id_user_selection = book_id_selection, iterable = books, iterable_name= "book")

            selected_book_id = selected_book['id']

            availability_data = get_book_availability(selected_book_id)

            print(f"\nThe following libraries have the following stock levels for {availability_data[0]['title']}, {availability_data[0]['author_name']}:")

            time.sleep(1)

            for book in availability_data:
                print()
                print(f'Location: {book["location"]}')
                print(f'Inventory: {book["inventory"]}')
                print(f'On Loan: {book["on_loan"]}')
                print(f'Available: {int(book["inventory"]) - int(book["on_loan"])}')
                time.sleep(1)

            return_to_menu()

    except Exception as e:
        print(e)

def book_information ():
    books = get_all_books()

    if books == "No available books":
        print("\nWe are unable to retrieve books data at this time. Returning to main menu.\n")
        time.sleep(1)
        return start_menu()
    else:
        print("\nPlease select a book to view further information:\n")

        time.sleep(1)

        for book in books:
            print(f"Book id: {book["id"]}, Book name: {book['title']}")

        time.sleep(1)

        book_id_selection = input("\nPlease type in your chosen book id to see further information.\n")

        selected_book = validate_user_selection(id_user_selection = book_id_selection, iterable = books, iterable_name= "book")

        selected_book_id = selected_book['id']

        book, book_genres = get_book_information(selected_book_id)

        if book == "No book data available":
            print("\nWe are unable to retrieve books data at this time. Returning to main menu.\n")
            time.sleep(1)
            return start_menu()

        print(f"\nThe listing details for {selected_book["title"]} includes:\n")
        time.sleep(1)

        book = book[0]

        for key, value in book.items():
            format_key = key.capitalize().replace('_', ' ')
            if key == "publication_date":
                publication_date = date_string_to_date_object(value)
                formatted_date = publication_date.strftime("%d %B %Y")
                print(f'{format_key}: {formatted_date}')
            elif key == "id":
                pass
            elif value is None:
                print(f"{format_key}: No {format_key.lower()} information on file")
            else:
                print(f'{key.capitalize().replace('_', ' ')}: {value}')

        try:
            genre_string = ""
            if book_genres == "No genres available":
                raise Exception("Genre: No genres information available")

            for genre in book_genres:
                genre_string = genre_string + f", {genre['genre']}"
            print(f"Genre: {genre_string[2:]}")
        except Exception as e:
            print(f"{e}")

        return_to_menu()

# Functions for the admin menu
def admin_add_customer():
    print("\nPlease enter the customer details")

    first_name = input("\nPlease enter the customers first name\n")
    last_name = input("\nPlease enter the customers last name\n")
    email_address = input("\nPlease enter the customers email address\n")
    street_address = input("\nPlease enter the customers street address\n")
    postcode = input("\nPlease enter the customers postal code\n")

    customer_dictionary = {
        "first_name" : first_name,
        "last_name" : last_name,
        "email_address" : email_address,
        "street_address" : street_address,
        "postcode" : postcode
    }

    post_add_customer(customer_dictionary)

    return_to_menu()

def admin_update_customer_details():
    print("\nPlease select a customer to update their values:\n")

    time.sleep(1)

    customers = get_all_customers()

    if customers == "No available customers.":
        print("There are no available customers at this time. Returning to main menu.\n")
        time.sleep(1)
        return start_menu()

    for customer in customers:
        print(f"Customer ID: {customer['id']}")
        print(f"First Name: {customer['first_name']}")
        print(f"Last Name: {customer['last_name']}")
        print()

    ids = [str(customer["id"]) for customer in customers]

    while True:
        selected_customer_id = input("Please enter a customer id to update their values:\n")

        if selected_customer_id not in ids:
            print("\nThis is not a valid customer id.")
        else:
            break

    selected_customer = ""
    for customer in customers:
        if customer["id"] == int(selected_customer_id):
            selected_customer = customer

    print(f"\nYou have selected {selected_customer['first_name']} {selected_customer['last_name']}.")

    print("\nPlease enter the updated customer details")

    def see_if_empty_string(string):
        if string == "":
            return None
        else:
            return string

    first_name = see_if_empty_string(input("\nPlease enter the updated first name or press enter to make no changes\n"))
    last_name = see_if_empty_string(input("\nPlease enter the customers last name or press enter to make no changes\n"))
    email_address = see_if_empty_string(input("\nPlease enter the customers email address or press enter to make no changes\n"))
    street_address = see_if_empty_string(input("\nPlease enter the customers street address or press enter to make no changes\n"))
    postcode = see_if_empty_string(input("\nPlease enter the customers postal code or press enter to make no changes\n"))

    customer_dictionary = {
        "first_name" : first_name,
        "last_name" : last_name,
        "email_address" : email_address,
        "street_address" : street_address,
        "postcode" : postcode
    }

    keys_to_remove = []
    for customer_detail in customer_dictionary:
        if customer_dictionary[customer_detail] is None:
            keys_to_remove.append(customer_detail)

    for key in keys_to_remove:
        del customer_dictionary[key]

    customer_dictionary["id"] = selected_customer["id"]

    put_update_customer(customer_dictionary)

    return_to_menu()

def admin_checkout_book():
    customers = get_all_customers()

    print("Welcome to the checkout book menu, please select a customer, library and book to checkout a book.")

    def replace_none(value, default_value="None"):
        return value if value is not None else default_value

    print("\nPlease find registered customers:")

    header = f"\n{'ID':<3} {'First Name':<15} {'Last Name':<15} {'Email Address':<40} {'Start Date':<20} {'End Date':<20} {'Street Address':<30} {'Postcode':<10}"
    print(header)
    print("-" * len(header))
    for customer in customers:
        membership_start_date = datetime.strptime(customer['membership_start_date'], "%a, %d %b %Y %H:%M:%S %Z")
        membership_start_date_formatted = membership_start_date.strftime("%d/%m/%Y")
        if customer['membership_end_date'] is None:
            membership_end_date_formatted = "None"
        else:
            membership_end_date = datetime.strptime(customer['membership_end_date'], "%a, %d %b %Y %H:%M:%S %Z")
            membership_end_date_formatted = membership_end_date.strftime("%d/%m/%Y")
        print(f"{replace_none(customer['id']):<3} {replace_none(customer['first_name']):<15} {replace_none(customer['last_name']):<15} {replace_none(customer['email_address']):<40} {membership_start_date_formatted:<20} {membership_end_date_formatted:<20} {replace_none(customer['street_address']):<30} {replace_none(customer['postcode']):<10}")

    customer_id = input("\nPlease select a customer id:\n")

    selected_customer = validate_user_selection(id_user_selection = customer_id, iterable = customers, iterable_name= "id")

    libraries = get_all_libraries()

    print("\nPlease see the available libraries:")
    header = f"\n{'ID':<3} {'Location':<20} {'Address':<50} {'Phone Number':<20} {'Website':<30} {'Email Address':<28}"
    print(header)
    print("-" * len(header))
    for library in libraries:
        print(f"{replace_none(library['id']):<3} {replace_none(library['location']):<20} {replace_none(library['address']):<50} {replace_none(library['phone_number']):<20} {replace_none(library['website']):<30} {replace_none(library['email']):<28}")

    library_id = input("\nPlease select a library id:\n")

    selected_library = validate_user_selection(id_user_selection = library_id, iterable = libraries, iterable_name= "library_id")

    books = get_available_books(selected_library['id'])

    print("\nPlease see the available books for the selected library")
    header = f"\n{'ID':<10} {'Title':<30} {'Author Name':<30} {'Inventory':<5}"
    print(header)
    print("-" * len(header))
    for book in books:
        print(f"{replace_none(book['id']):<10} {replace_none(book['title']):<30} {replace_none(book['author_name']):<30} {replace_none(book['inventory']):<5}")

    book_id = int(input("\nPlease select a book id:\n"))

    selected_book = validate_user_selection(id_user_selection=book_id, iterable=books,
                                               iterable_name="id")

    query_data = {
        'customer_id': int(selected_customer['id']),
        'book_id': int(selected_book['id']),
        'library_id': int(selected_library['id'])
    }

    post_checkout_book(query_data)

    return_to_menu()

def admin_outstanding_loans(mode=None):
    try:
        outstanding_loans = get_outstanding_loans()

        if outstanding_loans == "No available outstanding loans.":
            print("There are no available outstanding loans. Returning to main menu")
            return_to_menu()

        print("\nHere are the outstanding loans:\n")

        header = f"{'Loan ID':<7} {'Location':<20} {'Title':<30} {'Author Name':<20} {'Customer Name':<20} {'Loan Start Date':<16} {'Loan Due Date':<16}"
        print(header)

        print("-" * len(header))

        for loan in outstanding_loans:
            due_date = datetime.strptime(loan['loan_due_date'], "%a, %d %b %Y %H:%M:%S %Z")
            due_date_formatted = due_date.strftime("%d/%m/%Y")
            start_date = datetime.strptime(loan['loan_start_date'], "%a, %d %b %Y %H:%M:%S %Z")
            start_date_formatted = start_date.strftime("%d/%m/%Y")
            print(
                f"{loan['loan_id']:<7} {loan['location']:<20} {loan['title']:<30} {loan['author_name']:<20} {loan['customer_name']:<20} {start_date_formatted:<16} {due_date_formatted:<16}")

        if mode is None:
            return_to_menu()

    except Exception as e:
        print(f"An error occurred: {e}")

def admin_return_book():
    try:
        outstanding_loans = get_outstanding_loans()

        if outstanding_loans == "No available outstanding loans.":
            print("There are no available outstanding loans. Returning to main menu")
            return_to_menu()

        admin_outstanding_loans(mode="admin")

        try:
            return_id = int(input("\nPlease select a loan id to return:\n"))
        except:
            raise ValueError("\nThis is not a valid integer\n")

        print(f"\nYou have selected loan id: {return_id}")

        ids = [loan['loan_id'] for loan in outstanding_loans]

        if int(return_id) not in ids:
            raise ValueError("\nThis is not a valid loan id\n")

        return_date = input("\nPlease enter the return date in format dd-mm-yyyy or press enter if returned today:\n")

        if return_date.strip() == '':
            return_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(return_date)
        else:
            try:
                return_date = datetime.strptime(return_date, "%d-%m-%Y").strftime("%Y-%m-%d")
            except ValueError:
                raise ValueError("\nThis is not a valid return date\n")

        return_information = {
            "return_id": int(return_id),
            "return_date": return_date
        }

        put_return_book(return_information)

        return_to_menu()

    except ValueError as ve:
        print(f"{ve}")
        try_again = input("Would you like to try again (y/n)\n").lower().strip()
        if try_again == "y":
            admin_return_book()
        else:
            exit_application()

    except Exception as e:
        print(f"An error occurred: {e}")

def admin_overdue_books():
    try:
        overdue_books = get_overdue_books()

        if overdue_books == "No available overdue books.":
            print("There are no available overdue books. Returning to main menu")
            return_to_menu()

        print("\nHere are the overdue books:\n")

        header = f"{'Location':<20} {'Title':<30} {'Author Name':<20} {'Customer Name':<20} {'Customer Email Address':<30} {'Loan Start Date':<16} {'Loan Due Date':<16}"
        print(header)

        print("-" * len(header))

        for loan in overdue_books:
            due_date = datetime.strptime(loan['loan_due_date'], "%a, %d %b %Y %H:%M:%S %Z")
            due_date_formatted = due_date.strftime("%d/%m/%Y")
            start_date = datetime.strptime(loan['loan_start_date'], "%a, %d %b %Y %H:%M:%S %Z")
            start_date_formatted = start_date.strftime("%d/%m/%Y")
            print(
                f"{loan['location']:<20} {loan['title']:<30} {loan['author_name']:<20} {loan['customer_name']:<20} {loan['email_address']:<30} {start_date_formatted:<16} {due_date_formatted:<16}")

    except Exception as e:
        print(f"An error occurred: {e}")

    return_to_menu()

def admin_add_book():
    print("\nPlease enter the book details")

    title = input("\nPlease enter the book title:\n")
    author_first_name = input("\nPlease enter the authors first name:\n")
    author_surname = input("\nPlease enter the authors surname:\n")

    year = ""
    year_integer = False
    four_digit_year = False
    while not year_integer and not four_digit_year:
        try:
            year = input("\nPlease enter the book year of printing:\n")

            regex_pattern = r'^\d{4}$'
            four_digit_year = bool(re.match(regex_pattern, year))

            year = int(year)
            year_integer = True
        except ValueError:
            print("\nThis is not a valid year, please try again ensuring the year is in format YYYY.")

    pages = ""
    pages_integer = False
    while not pages_integer:
        try:
            pages = int(input("\nPlease enter the number of pages:\n"))
            pages_integer = True
        except ValueError:
            print("\nThis is not a valid number of pages, please try again.")

    publisher = input("\nPlease enter the publisher:\n")

    publication_date = ""
    publication_date_is_date = False
    while not publication_date_is_date:
        try:
            publication_date = input("\nPlease enter the original publication date:\n")
            date_format = "%Y-%m-%d"
            datetime.strptime(publication_date, date_format)
            publication_date_is_date = True
        except ValueError:
            print("\nThis is not a valid date format, please enter a date in the format YYYY-MM-DD")

    isbn_correctly_formatted = False
    isbn =""
    while not isbn_correctly_formatted:
        isbn = input("\nPlease enter the books ISBN (in format: 978-3161484100):\n")
        regex_pattern = r'^\d{3}-\d{10}$'
        isbn_correctly_formatted = bool(re.match(regex_pattern, isbn))
        if not isbn_correctly_formatted:
            print("\nThis is not a valid ISBN number, please try again.")

    book_dictionary = {
        "title" : title,
        "author_first_name" : author_first_name,
        "author_surname" : author_surname,
        "year" : year,
        "pages" : pages,
        "publisher" : publisher,
        "publication_date" : publication_date,
        "isbn" : isbn
    }

    post_add_book(book_dictionary)

    return_to_menu()

def admin_delete_book_by_id():
    books = get_all_books()

    if books == "No available books":
        print("\nWe are unable to retrieve books data at this time. Returning to main menu.\n")
        time.sleep(1)
        return start_menu()
    else:
        print("\nPlease select a book to delete from the library catalogue:\n")

        time.sleep(1)

        for book in books:
            print(f"Book id: {book["id"]}, Book name: {book['title']}")

        time.sleep(1)

        book_id_selection = input("\nPlease type in your chosen book id to delete from the database.\n")

        selected_book = validate_user_selection(id_user_selection=book_id_selection, iterable=books,
                                                iterable_name="book")

        selected_book_id = {'book_id': int(selected_book['id'])}

        delete_delete_book(selected_book_id)

        return_to_menu()

menu_options = [
    {"id": 1, "function": library_locations, "menu option": "See library locations"},
    {"id": 2, "function": available_books, "menu option": "See available books at a library"},
    {"id": 3, "function": book_availability, "menu option": "Check book availability"},
    {"id": 4, "function": book_information, "menu option": "See book information"},
    {"id": 5, "function": admin_actions, "menu option": "Admin"},
    {"id": 6, "function": exit_application, "menu option": "Exit"}
]

admin_menu_options = [
    {"id": 1, "function": admin_add_customer, "menu option": "Add a customer"},
    {"id": 2, "function": admin_update_customer_details, "menu option": "Update customer details"},
    {"id": 3, "function": admin_checkout_book, "menu option": "Checkout a book"},
    {"id": 4, "function": admin_return_book, "menu option": "Return an item"},
    {"id": 5, "function": admin_outstanding_loans, "menu option": "See outstanding loans"},
    {"id": 6, "function": admin_overdue_books, "menu option": "See overdue books"},
    {"id": 7, "function": admin_add_book, "menu option": "Add a book"},
    {"id":8, "function": admin_delete_book_by_id, "menu option": "Delete a book"},
    {"id": 9, "function": return_to_menu, "menu option": "Return to main menu"}
]

def start_menu():
    print_welcome()
    check_server_running()
    print_menu()
    menu_selector()

if __name__ == "__main__":
    start_menu()



