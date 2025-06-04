![image](https://github.com/user-attachments/assets/0d700c3b-b245-4189-943f-3dbc47028b46)

# Assignment 4: APIs

### Welcome to the Warwickshire library API
For this project I have opted to emulate a library system. I have created a library database with tables for:
- Customers
- Libraries
- Customer Loans
- Books
- Book Genres

I used the mysql-python-connector to connect my database utils to the MySQL database and retrieve customer information.

I have opted to use a parameterized query when executing queries in order to prevent SQL injection attacks.

I have created an API with the following endpoints:
- '/' - index endpoint, welcoming user to the API
- '/libraries' - endpoint which 'gets' all library information for the database
- '/libraries/<int:library_id>' - endpoint which 'gets' information for a single library, selected by library id
- '/books' - endpoint which 'gets' all books in all libraries
- '/books/<int:book_id>' - endpoint which 'gets' information for a specific book
- '/libraries/<int:library_id>/books' - endpoint which 'gets' the books for a given library
- '/books/<int:book_id>/genres' - endpoint which 'gets' the books genre information for a given book id
- '/book_availability/<int:book_id>' - endpoint which 'gets' the book availability for a given book id
- '/customers' - endpoint which 'gets' all the customers
- '/outstanding_loans' - endpoint which 'gets' any customers with an outstanding book loan
- '/overdue_books' - endpoint which 'gets' any customers with an overdue book
- '/add_customer' - endpoint which 'posts' a customer details to the database
- '/update_customer' - endpoint which 'puts' data into the database, updating a given customer
- '/checkout_book' - endpoint which 'posts' information to the database, enabling a book to be loaned
- '/return_book' - endpoint which 'puts' data into the database, updating an open customer loan
- '/add_book' - endpoint which 'posts' a book details to the database
- '/delete_book' - endpoint which 'deletes' a book from the database

### Setup
In order to set up the database you need to:
1. Open the three MySQL files in MySQL and run them in the following order:
   - libraries_database_schema
   - libraries_database_trigger
   - libraries_database_data
2. Open the python files and edit the config.py file to change:
   - HOST='your_host'
   - USER='your_user'
   - PASSWORD='your_password'
3. Ensure that the requirements.txt is installed:
   - This can be achieved in pycharm terminal using the ``pip install -r requirements.txt
`` command
   - Alternately, you can locate the requirements.txt file in the Pycharm project directory, right-click on the file and right-click on requirements.txt. From the context menu, select Install requirements.
4. Run the libraries_api_server - this will run the server in debug mode and allow for communication from the client side 
5. Run the main.py file - this is an implementation of the client side of the application which interacts with the database via the API endpoints and retrieves/sends data displaying it in a console application. 

### Testing
As I was writing the API I performed a selection of functional tests on the API endpoints in postman. I have attached my postman tests to the GitHub Repo.

In addition, I performed unit test on the client side and API side for the get libraries function.


