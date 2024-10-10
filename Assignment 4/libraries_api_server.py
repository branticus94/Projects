from flask import Flask, jsonify, request
from flask_cors import CORS

from db_error_handling import get_all_libraries, get_books_from_a_library, get_all_books, get_book_information_by_id, \
    get_genre_information, get_library_information, check_book_availability, insert_new_customer, update_customer, \
    get_all_customers, checkout_book, return_book, see_overdue_books, insert_new_book, delete_book
from db_error_handling import see_outstanding_loans

app = Flask(__name__)

CORS(app)

@app.route('/', methods=['GET'])
def index():
    return {"message":"Welcome to the Library API! Here you will be able to interact with the Warwickshire Library Database and retrieve information."}

@app.route('/libraries', methods=['GET'])
def get_libraries():
    try:
        libraries =  get_all_libraries()

        if not libraries:
            return jsonify({"An error occurred": "No libraries found"}), 404

        return jsonify(libraries), 200

    except Exception as e:
        return jsonify({'An error occurred': str(e)}), 500

@app.route('/libraries/<int:library_id>', methods=['GET'])
def get_library_data(library_id):
    try:
        library =  get_library_information(library_id)

        if not library:
            return jsonify({"An error occurred": "No library found"}), 404

        return jsonify(library), 200

    except Exception as e:
        return jsonify({'An error occurred': str(e)}), 500

@app.route('/libraries/<int:library_id>/books', methods=['GET'])
def get_books_from_id_library(library_id):
    try:
        books = get_books_from_a_library(library_id = library_id)

        if not books:
            return jsonify({"An error occurred": "No book with that id found"}), 404

        return jsonify(books), 200
    except Exception as e:
        return jsonify({'An error occurred': str(e)}), 500

@app.route('/books', methods=['GET'])
def get_books_information():
    try:
        books = get_all_books()

        if not books:
            return jsonify({"An error occurred": "No books found"}), 404

        return jsonify(books), 200

    except Exception as e:
        return jsonify({'An error occurred': str(e)}), 500

@app.route('/books/<int:book_id>', methods=['GET'])
def get_book_information(book_id):
    try:
        book = get_book_information_by_id(book_id)

        if not book:
            return jsonify({"An error occurred": "No book with that id found"}), 404

        return jsonify(book), 200
    except Exception as e:
        return jsonify({'An error occurred': str(e)}), 500

@app.route('/books/<int:book_id>/genres', methods=['GET'])
def get_genre(book_id):
    try:
        genre = get_genre_information(book_id)

        if not genre:
            return jsonify({"An error occurred": "No genre information found"}), 404

        return jsonify(genre), 200

    except Exception as e:
        return jsonify({'An error occurred': str(e)}), 500

@app.route('/book_availability/<int:book_id>', methods=['GET'])
def get_book_availability(book_id):
    try:
        availability = check_book_availability(book_id)

        if not availability:
            return jsonify({"An error occurred": "No book availability found"}), 404

        return jsonify(availability), 200
    except Exception as e:
        return jsonify({'An error occurred': str(e)}), 500

@app.route('/customers', methods=['GET'])
def get_customers():
    try:
        customers = get_all_customers()

        if not customers:
            return jsonify({"An error occurred": "No customers found"}), 404

        return jsonify(customers), 200
    except Exception as e:
        return jsonify({'An error occurred': str(e)}), 500

@app.route('/add_customer', methods=['POST'])
def post_customer():
    try:
        customer_data = request.get_json()
        insert_new_customer(customer_data)
        return jsonify({"message": "Customer added successfully"}), 201

    except ValueError as ve:
        return jsonify({'error': f'Value error: {str(ve)}'}), 400

    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500

@app.route('/update_customer', methods=['PUT'])
def put_customer_details():
    try:
        updated_customer_data = request.get_json()
        update_customer(updated_customer_data)
        return jsonify({"message": "Customer updated successfully"}), 201

    except ValueError as ve:
        return jsonify({'error': f'Value error: {str(ve)}'}), 400

    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500

@app.route('/checkout_book', methods=['POST'])
def post_checkout_book():
    try:
        checkout_information = request.get_json()
        checkout_book(checkout_information)
        return jsonify({"message": "Book checked-out successfully"}), 201

    except ValueError as ve:
        return jsonify({'error': f'Value error: {str(ve)}'}), 400

    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500

@app.route('/return_book', methods=['PUT'])
def put_return_book():
    try:
        return_information = request.get_json()
        return_book(return_information)
        return jsonify({"message": "Book returned successfully"}), 201

    except ValueError as ve:
        return jsonify({'error': f'Value error: {str(ve)}'}), 400

    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500

@app.route('/outstanding_loans', methods=['GET'])
def get_outstanding_loans():
    try:
        outstanding_loans = see_outstanding_loans()
        return jsonify(outstanding_loans), 200

    except ValueError as ve:
        return jsonify({'error': f'Value error: {str(ve)}'}), 400

    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500

@app.route('/overdue_books', methods=['GET'])
def get_overdue_books():
    try:
        overdue_books = see_overdue_books()
        return jsonify(overdue_books), 200

    except ValueError as ve:
        return jsonify({'error': f'Value error: {str(ve)}'}), 400

    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500

@app.route('/add_book', methods=['POST'])
def post_add_book():
    try:
        book_information = request.get_json()
        insert_new_book(book_information)
        return jsonify({"message": "Book inserted successfully"}), 201

    except ValueError as ve:
        return jsonify({'error': f'Value error: {str(ve)}'}), 400

    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500

@app.route('/delete_book', methods=['DELETE'])
def delete_book_by_id():
    try:
        book_id = request.get_json()
        delete_book(book_id)
        return jsonify({"message": "Book deleted successfully"}), 204

    except ValueError as ve:
        return jsonify({'error': f'Value error: {str(ve)}'}), 400

    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True)
