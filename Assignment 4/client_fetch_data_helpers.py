import requests

BASE_URL = 'http://127.0.0.1:5000'

def fetch_data(url, error_message):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return error_message

def delete_data(url, json_data, error_message):
    try:
        response = requests.delete(url, json = json_data)
        if response.status_code == 204:
            print("\nOperation successful.")
        else:
            print(f"{error_message} (Status Code: {response.status_code})")
    except Exception as e:
        print(f"An error occurred: {e}")

def post_data(url, json_data, error_message):
    try:
        response = requests.post(url, json=json_data)
        if response.status_code == 201:
            print("\nOperation successful.")
        else:
            print(f"\n{error_message} {response.json()["error"]}")
    except Exception as e:
        print(f"An error occurred: {e}")

def put_data(url, json_data, error_message):
    try:
        response = requests.put(url, json=json_data)
        if response.status_code == 201:
            print("\nOperation successful.")
        else:
            print(f"Failed to update: {error_message} (Status Code: {response.status_code} {response.text})")
    except Exception as e:
        print(f"An error occurred: {e}")

def get_index():
    return fetch_data(f'{BASE_URL}/', "The server is not running")

def get_all_libraries():
    return fetch_data(f'{BASE_URL}/libraries', "No available libraries")

def get_available_books(selected_library_id):
    return fetch_data(f'{BASE_URL}/libraries/{selected_library_id}/books', "No available books")

def get_all_books():
    return fetch_data(f'{BASE_URL}/books', "No available books")

def get_book_availability(selected_book_id):
    return fetch_data(f'{BASE_URL}/book_availability/{selected_book_id}', "No availability data available")

def get_book_information(selected_book_id: int):
    book_info = fetch_data(f'{BASE_URL}/books/{selected_book_id}', "No book data available")
    if book_info == "No book information data available":
        return "No book data available", "No genres available"

    book_genres = fetch_data(f'{BASE_URL}/books/{selected_book_id}/genres', "No genres available")
    return book_info, book_genres

def get_all_customers():
    return fetch_data(f'{BASE_URL}/customers', "No available customers.")

def get_outstanding_loans():
    return fetch_data(f'{BASE_URL}/outstanding_loans', "No available outstanding loans.")

def get_overdue_books():
    return fetch_data(f'{BASE_URL}/overdue_books', "No available overdue books.")

def delete_delete_book(selected_book_id):
    delete_data(f'{BASE_URL}/delete_book', json_data = selected_book_id, error_message= f"Failed to delete book with ID {selected_book_id}")

def post_add_book(book_dictionary):
    post_data(f'{BASE_URL}/add_book', book_dictionary, "Failed to add book.")

def put_return_book(return_information):
    put_data(f'{BASE_URL}/return_book', return_information, "Failed to return book.")

def put_update_customer(customer_dictionary):
    put_data(f'{BASE_URL}/update_customer', customer_dictionary, "Failed to update customer.")

def post_add_customer(customer_dictionary):
    post_data(f'{BASE_URL}/add_customer', customer_dictionary, "Failed to add customer.")

def post_checkout_book(query_data):
    post_data(f'{BASE_URL}/checkout_book', query_data, "Failed to checkout book.")
