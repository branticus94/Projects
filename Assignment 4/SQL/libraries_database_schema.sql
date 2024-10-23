-- DROP DATABASE libraries_database;

CREATE DATABASE IF NOT EXISTS libraries_database;

USE libraries_database;

CREATE TABLE IF NOT EXISTS libraries(
	id INT PRIMARY KEY AUTO_INCREMENT,
	location VARCHAR(100) NOT NULL, 
    address VARCHAR(255),
    phone_number VARCHAR(15),
    website VARCHAR(255), 
    email VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS books(
	id INT AUTO_INCREMENT PRIMARY KEY,
	title VARCHAR(255) NOT NULL,
	author_first_name VARCHAR(255),
    author_surname VARCHAR(255), 
	year INT,
	pages INT, 
	publisher VARCHAR(255),
	publication_date DATE ,
	isbn VARCHAR(14)
);

CREATE TABLE IF NOT EXISTS genres(
	id INT AUTO_INCREMENT PRIMARY KEY,
    genre_name VARCHAR(255) UNIQUE
);

CREATE TABLE IF NOT EXISTS book_genres(
	book_id INT,
    genre_id INT,
    FOREIGN KEY (book_id) REFERENCES books(id) ON DELETE CASCADE,
    FOREIGN KEY (genre_id) REFERENCES genres(id),
    PRIMARY KEY (book_id, genre_id)
);

CREATE TABLE IF NOT EXISTS library_books(
	library_id INT,
    book_id INT,
	FOREIGN KEY (book_id) REFERENCES books(id) ON DELETE CASCADE,
    FOREIGN KEY (library_id) REFERENCES libraries(id)
);

CREATE TABLE IF NOT EXISTS customers(
	id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email_address VARCHAR(255),
    street_address VARCHAR(255),
    postcode VARCHAR(10),
    membership_start_date DATETIME DEFAULT NOW(),
    membership_end_date DATETIME DEFAULT NULL
);

CREATE TABLE IF NOT EXISTS customer_loans(
	id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT,
    book_id INT,
    library_id INT,
    loan_start_date TIMESTAMP NOT NULL DEFAULT NOW(),
    loan_due_date TIMESTAMP NOT NULL,
    return_date TIMESTAMP,
    FOREIGN KEY (book_id) REFERENCES books(id) ON DELETE SET NULL,
    FOREIGN KEY (library_id) REFERENCES libraries(id),
    FOREIGN KEY (customer_id) REFERENCES customers(id)
);