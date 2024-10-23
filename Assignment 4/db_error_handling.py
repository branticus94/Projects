from validate_email_address import validate_email

from db_utils import execute_query
from datetime import datetime
import re

def _is_valid_datetime_date(date_string):
    try:
        datetime.strptime(date_string, "%Y-%m-%d")
        return True
    except ValueError:
        raise ValueError("Date is not in correct format.")

def _get_headers(table_name):
    try:
        query_string = f'DESC {table_name};'

        headers_query_data = execute_query(query_string)

        headers = [header[0] for header in headers_query_data]

        return headers
    except Exception as e:
        print(f"An error occurred while retrieving headers for table '{table_name}': {str(e)}")
        return None

def _combine(headers, records):

    records_dictionary_list = []

    for record in records:
        record_dictionary = dict(map(lambda x, y: (x, y), headers, record))
        records_dictionary_list.append(record_dictionary)

    return records_dictionary_list

def get_all_libraries():
    """
    Retrieve all library records from the libraries database table.

    Returns:
        list: A list of library records.
    """
    try:
        headers = _get_headers('libraries')

        all_libraries_query_data = execute_query('SELECT * FROM libraries')

        if all_libraries_query_data == []:
            raise Exception ("No libraries information found")

        libraries_list = [library for library in all_libraries_query_data]

        libraries = _combine(headers = headers, records = libraries_list)

        return libraries
    except Exception as e:
        raise e

def get_library_information(library_id):
    """
    Retrieve all library information for a specific library from the libraries database table.

    Returns:
        list: A list of library records.
    """
    try:
        headers = _get_headers('libraries')

        query_string = 'SELECT * FROM libraries WHERE id = %s'

        library_id = (library_id,)

        library_query_data = execute_query(query_string, library_id)

        if not library_query_data:
            raise Exception("No library information found")

        library = _combine(headers = headers, records = library_query_data)

        return library

    except Exception as e:
        raise e

def get_all_books():
    """
    Retrieve all book information from the books database table.

    Returns:
        list: A list of book records.
    """
    try:
        headers = _get_headers('books')

        all_books_query_data = execute_query('SELECT * FROM books')

        if not all_books_query_data:
            raise Exception ("No books information found")

        books_list = [book for book in all_books_query_data]

        books = _combine(headers = headers, records = books_list)

        return books
    except Exception as e:
        raise e

def get_book_information_by_id(book_id):
    """
    Retrieve all book information from the books database table.

    Returns:
        list: A list of book information.
    """
    try:
        headers = _get_headers('books')

        book_id = (book_id,)

        query_string = 'SELECT * FROM books WHERE id = %s'

        book_query_data = execute_query(query_string, book_id)

        if not book_query_data:
            raise Exception("No information found for the given book")

        book = _combine(headers = headers, records = book_query_data)

        return book

    except Exception as e:
        raise e

def get_books_from_a_library(library_id):
    """
        Retrieve the names and inventory of all books for a particular library.

        Returns:
            list: A list of books stocked at a particular library .
    """
    try:
        headers = ['id', 'title', 'author_name', 'inventory']

        query_string = "SELECT b.id, b.title, CONCAT(b.author_first_name,' ', b.author_surname) AS author_name, COUNT(*) as quantity FROM library_books lb  INNER JOIN libraries l  ON lb.library_id = l.id  INNER JOIN books b  ON lb.book_id = b.id WHERE l.id = %s GROUP BY book_id;"

        library_id = (library_id,)

        books_from_library_query_data = execute_query(query_string, library_id)

        if not books_from_library_query_data:
            raise Exception("No books found for the given library")

        books_list = [book for book in books_from_library_query_data]

        books = _combine(headers=headers, records=books_list)

        return books

    except Exception as e:
        raise e

def get_genre_information(book_id):
    """
    Retrieve all genres for a given book from the genres-book database table.

    Returns:
        list: A list of genres for a specified book.
    """
    try:
        query_string = 'SELECT genre_name FROM books b INNER JOIN book_genres bg ON b.id = bg.book_id INNER JOIN genres g ON g.id = bg.genre_id WHERE b.id = %s;'

        book_id = (book_id,)

        all_genres_query_data = execute_query(query_string, book_id)

        if not all_genres_query_data:
            raise Exception("No genres found for the given book")

        genres_list = [genre[0] for genre in all_genres_query_data]

        genres_dictionary_list = [{"genre": genre} for genre in genres_list]

        return genres_dictionary_list

    except Exception as e:
        raise e

def check_book_availability(book_id):
    """
    Search the catalogue to see where a given book is in stock.

    Returns:
        list: A list of availability for a specified book.
    """
    try:
        query_string = 'WITH library_inventory AS(SELECT lb.library_id, lb.book_id, l.location,b.title,CONCAT(b.author_first_name," ",b.author_surname) AS author_name,COUNT(*) as inventory FROM library_books lb INNER JOIN books b ON lb.book_id = b.id INNER JOIN libraries l ON l.id = lb.library_id GROUP BY library_id, lb.book_id),customer_loans AS(SELECT cl.library_id,cl.book_id,COUNT(*) as on_loan FROM customer_loans cl WHERE return_date is NULL GROUP BY cl.book_id, cl.library_id)SELECT li.title,li.author_name,li.location,li.library_id,li.book_id,li.inventory,IFNULL(cl.on_loan,0) as on_loan FROM library_inventory li LEFT JOIN customer_loans cl ON li.library_id = cl.library_id AND li.book_id = cl.book_id HAVING li.book_id = %s;'

        book_id = (book_id,)

        headers = ['title', 'author_name', 'location', 'library_id', 'book_id', 'inventory', 'on_loan', 'available']

        book_availability_query_data = execute_query(query_string, book_id)

        if not book_availability_query_data:
            raise Exception("No availability found for the given book")

        book_availability = [book for book in book_availability_query_data]

        books = _combine(headers=headers, records=book_availability)

        return books

    except Exception as e:
        raise e

def get_all_customers():
    """
    Retrieve all customer information from the customers database table.

    Returns:
        list: A list of customer records.
    """
    try:
        headers = _get_headers('customers')

        all_customers_query_data = execute_query('SELECT * FROM customers')

        if not all_customers_query_data:
            raise Exception ("No customers found.")

        customers_list = [customer for customer in all_customers_query_data]

        customers = _combine(headers = headers, records = customers_list)

        return customers
    except Exception as e:
        raise e

def insert_new_customer(customer_information):
    """
        Add a customer to the customers table validating user input and handling errors.
    """
    try:
        required_fields = ['first_name', 'last_name']
        if not all(k in customer_information for k in required_fields):
            raise ValueError("Record is missing required fields")

        for key in customer_information:
            if type(customer_information[key]) is not str:
                raise ValueError("Record has an unexpected data type for one of the required fields")

        if customer_information.get("email_address") is not None:
            if validate_email(customer_information.get("email_address")) is False:
                raise ValueError("Email address is invalid.")

        insertion_order = ['first_name', 'last_name', 'email_address', 'street_address', 'postcode']

        customer_details = tuple([customer_information.get(key, None) for key in insertion_order])

        sql_query = "INSERT INTO customers (first_name, last_name, email_address, street_address, postcode) VALUES (%s, %s, %s, %s, %s);"

        execute_query(sql_query, customer_details, query_type="POST")

    except ValueError as ve:
        raise ve
    except Exception as e:
        raise e

def update_customer(updated_customer_information):
    updated_customer_id = updated_customer_information.get('id')

    try:
        if type(updated_customer_id) is not int:
            raise ValueError("Customer id is required to update the record.")

        type_schema = {
            'id': int,
            'first_name':str,
            'last_name':str,
            'email_address':str,
            'street_address':str,
            'postcode':str,
            'membership_start_date':str,
            'membership_end_date':str
        }

        for key in updated_customer_information:
            if type(updated_customer_information[key]) is not type_schema[key]:
                raise ValueError("Record has an unexpected data type for one or more of the required fields")

        if updated_customer_information.get("membership_start_date") is not None:
            _is_valid_datetime_date(updated_customer_information.get("membership_start_date"))

        if updated_customer_information.get("membership_end_date") is not None:
            _is_valid_datetime_date(updated_customer_information.get("membership_end_date"))

        if updated_customer_information.get("email_address") is not None:
            if validate_email(updated_customer_information.get("email_address")) is False:
                raise ValueError("Email address is invalid.")

        insertion_order = ['first_name', 'last_name', 'email_address', 'street_address', 'postcode', 'membership_start_date', 'membership_end_date']

        ordered_keys = [item for item in insertion_order if item in updated_customer_information]
        ordered_customer_details = [updated_customer_information[item] for item in ordered_keys]

        set_clauses = [f"{key} = %s" for key in ordered_keys]
        sql_query = f"UPDATE customers SET {', '.join(set_clauses)} WHERE id = %s"
        query_data = ordered_customer_details + [updated_customer_id]

        execute_query(sql_query, query_data, query_type='PUT')

    except ValueError as ve:
        raise ve
    except Exception as e:
        raise e

def checkout_book(checkout_information):
    try:
        type_schema = {
            'customer_id': int,
            'book_id': int,
            'library_id': int,
            'loan_start_date': str
        }

        for key in checkout_information:
            if type(checkout_information[key]) is not type_schema[key]:
                raise ValueError("Record has an unexpected data type for one of the required fields")

        if checkout_information.get("loan_start_date") is not None:
            _is_valid_datetime_date(checkout_information.get("loan_start_date"))

        library_ids = get_all_libraries()
        library_ids = [library['id'] for library in library_ids]

        if checkout_information.get("library_id") not in library_ids:
            raise ValueError("This is not a valid library, please try again.")

        books_from_library = get_books_from_a_library(checkout_information.get("library_id"))
        books_from_library = [book['id'] for book in books_from_library]

        if checkout_information.get("book_id") not in books_from_library:
            raise ValueError("This is not a valid book selection, please try again.")

        availability = check_book_availability(checkout_information['book_id'])
        availability = [availability for availability in availability if availability['library_id'] == checkout_information['library_id']]
        if (int(availability[0]['inventory']) - int(availability[0]['on_loan']))<=0:
            raise ValueError("The selected book is not in stock at the minute, please try again.")

        key_order = ['customer_id', 'book_id', 'library_id', 'loan_start_date']

        ordered_keys = [item for item in key_order if item in checkout_information.keys()]
        ordered_checkout_details = [checkout_information[item] for item in ordered_keys]

        keys = f"({', '.join(ordered_keys)})"
        value_placeholders = f"({('%s, ' * len(ordered_checkout_details))[:-2]})"

        sql_query = f"""INSERT INTO customer_loans {keys} VALUES {value_placeholders};"""
        query_data = tuple(ordered_checkout_details)

        execute_query(sql_query, query_data, query_type="POST")

    except ValueError as ve:
        raise ve
    except Exception as e:
        raise e

def see_outstanding_loans():
    """
    Retrieve all customer loans which have not yet been returned .

    Returns:
        list: A list of outstanding customer loans.
    """
    try:
        headers = ['loan_id', 'location', 'title', 'author_name', 'customer_name', 'loan_start_date', 'loan_due_date']

        customer_loans = execute_query("SELECT cl.id AS loan_id, location, b.title, CONCAT(b.author_first_name, ' ', b.author_surname) AS author_name, CONCAT(c.first_name, ' ', c.last_name) AS customer_name, cl.loan_start_date, cl.loan_due_date FROM customer_loans cl INNER JOIN customers c ON c.id = cl.customer_id INNER JOIN books b ON b.id = cl.book_id INNER JOIN libraries l ON l.id = cl.library_id WHERE return_date IS NULL;")

        if not customer_loans:
            raise Exception ("No customer loans found.")

        customer_loans = [customer for customer in customer_loans]

        customer_loans = _combine(headers = headers, records = customer_loans)

        return customer_loans
    except Exception as e:
        raise e

def see_overdue_books():
    try:
        headers = ['location', 'title', 'author_name', 'customer_name', 'email_address', 'loan_start_date', 'loan_due_date']

        overdue_books_query = execute_query("SELECT l.location, b.title, CONCAT(b.author_first_name, ' ', b.author_surname) AS author_name, CONCAT(c.first_name, ' ', c.last_name) AS customer_name, c.email_address, cl.loan_start_date, cl.loan_due_date FROM customer_loans cl INNER JOIN customers c ON c.id = cl.customer_id INNER JOIN books b ON b.id = cl.book_id INNER JOIN libraries l ON l.id = cl.library_id WHERE return_date IS NULL and NOW()>loan_due_date;")

        if not overdue_books_query:
            raise Exception ("No overdue books found.")

        overdue_books = [book for book in overdue_books_query]

        overdue_books = _combine(headers = headers, records = overdue_books)

        return overdue_books
    except Exception as e:
        raise e

def return_book(return_information):
    try:
        try:
            int(return_information['return_id'])
        except ValueError:
            raise ValueError("Return ID must be a valid integer")

        if return_information.get("return_date") is not None:
            _is_valid_datetime_date(return_information.get("return_date"))
        else:
            raise ValueError("Date is required to return a book.")

        if return_information.get("return_id") is None:
            raise ValueError("Loan ID is required to return a book.")

        outstanding_loans = see_outstanding_loans()
        outstanding_loans = [loan['loan_id'] for loan in outstanding_loans]

        if return_information.get("return_id") not in outstanding_loans:
            raise ValueError("This return id is invalid. Either the loan does not exist or the book has already been returned.")

        sql_query = f"""UPDATE customer_loans SET return_date = %s WHERE id = %s;"""
        query_data = tuple((return_information['return_date'], return_information['return_id']))

        execute_query(sql_query, query_data, query_type="POST")

    except ValueError as ve:
        raise ve

    except Exception as e:
        raise e

def insert_new_book(new_book_information):
    """
        Add a book to the books table validating user input and handling errors.
    """
    try:
        if 'title' not in new_book_information:
            raise ValueError("Record is missing required fields - book title")

        type_schema = {
            'title': str,
            'author_first_name': str,
            'author_surname': str,
            'year': int,
            'pages': int,
            'publisher': str,
            'publication_date': str,
            'isbn': str
        }

        for key in new_book_information:
            if type(new_book_information[key]) is not type_schema[key]:
                raise ValueError("Record has an unexpected data type for one or more of the record fields")

        if 'isbn' in new_book_information:
            regex_pattern = r'^\d{3}-\d{10}$'

            def check_isbn_format(isbn):
                return bool(re.match(regex_pattern, isbn))

            is_isbn_formatted = check_isbn_format(new_book_information['isbn'])

            if not is_isbn_formatted:
                raise ValueError("Invalid ISBN format")

        insertion_order = ['title', 'author_first_name', 'author_surname', 'year', 'pages', 'publisher', 'publication_date', 'isbn']
        book_details = tuple([new_book_information.get(key, None) for key in insertion_order])

        sql_query = "INSERT INTO books (title, author_first_name, author_surname, year, pages, publisher, publication_date, isbn) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"

        execute_query(sql_query, book_details, query_type="POST")

    except ValueError as ve:
        raise ve
    except Exception as e:
        raise e

def delete_book(book):
    try:
        try:
            int(book['book_id'])
        except ValueError:
            raise ValueError("Book ID must be a valid integer")

        book_id = (book['book_id'], )

        sql_query = "DELETE FROM books WHERE id = %s;"

        execute_query(sql_query, book_id, query_type="DELETE")

    except ValueError as ve:
        raise ve
    except Exception as e:
        raise e