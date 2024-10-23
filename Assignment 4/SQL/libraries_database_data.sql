USE libraries_database;

INSERT INTO libraries 
(location, address, phone_number, website, email) 
VALUES
('Stratford-upon-Avon', 'Shakespeare Ave, Stratford-upon-Avon, CV37 6GP', '01789 293 485', 'www.stratfordlibrary.co.uk', 'info@stratfordlibrary.co.uk'),
('Warwick', 'Market Place, Warwick, CV34 4SA', '01926 492 212', 'www.warwicklibrary.co.uk', 'info@warwicklibrary.co.uk'),
('Leamington Spa', 'The Parade, Leamington Spa, CV32 4AT', '01926 742 700', 'www.leamingtonlibrary.co.uk', 'info@leamingtonlibrary.co.uk'),
('Henley-in-Arden', 'High Street, Henley-in-Arden, B95 5BX', '01564 792 355', 'www.henleylibrary.co.uk', 'info@henleylibrary.co.uk');

INSERT INTO genres 
(genre_name) 
VALUES
('Fiction'),
('Non-Fiction'),
('Fantasy'),
('Science Fiction'),
('Mystery'),
('Thriller'),
('Romance'),
('Biography'),
('Self-Help'),
('Historical Fiction');

INSERT INTO 
books 
(title, author_first_name, author_surname, year, pages, publisher, publication_date, isbn) 
VALUES
('The Hobbit', 'J.R.R.', 'Tolkien', 1937, 310, 'George Allen & Unwin', '1937-09-21', '978-0345339683'),
('1984', 'George', 'Orwell', 1949, 328, 'Secker & Warburg', '1949-06-08', '978-0451524935'),
('To Kill a Mockingbird', 'Harper', 'Lee', 1960, 281, 'J.B. Lippincott & Co.', '1960-07-11', '978-0061120084'),
('Pride and Prejudice', 'Jane', 'Austen', 1813, 432, 'T. Egerton', '1813-01-28', '978-1503290563'),
('The Great Gatsby', 'F. Scott', 'Fitzgerald', 1925, 180, 'Charles Scribner\'s Sons', '1925-04-10', '978-0743273565'),
('Moby Dick', 'Herman', 'Melville', 1851, 635, 'Harper & Brothers', '1851-11-14', '978-1503280786'),
('War and Peace', 'Leo', 'Tolstoy', 1869, 1225, 'The Russian Messenger', '1869-01-01', '978-1420954405'),
('The Catcher in the Rye', 'J.D.', 'Salinger', 1951, 277, 'Little, Brown and Company', '1951-07-16', '978-0316769488'),
('Brave New World', 'Aldous', 'Huxley', 1932, 268, 'Chatto & Windus', '1932-08-01', '978-0060850524'),
('Fahrenheit 451', 'Ray', 'Bradbury', 1953, 158, 'Ballantine Books', '1953-10-19', '978-1451673319'),
('The Picture of Dorian Gray', 'Oscar', 'Wilde', 1890, 254, 'Lippincott\'s Monthly Magazine', '1890-07-01', '978-1505291666'),
('The Brothers Karamazov', 'Fyodor', 'Dostoevsky', 1880, 796, 'The Russian Messenger', '1880-01-01', '978-0486454115'),
('Jane Eyre', 'Charlotte', 'Brontë', 1847, 500, 'Smith, Elder & Co.', '1847-10-16', '978-1503278197'),
('Wuthering Heights', 'Emily', 'Brontë', 1847, 348, 'Thomas Cautley Newby', '1847-01-01', '978-1505243304'),
('Crime and Punishment', 'Fyodor', 'Dostoevsky', 1866, 430, 'The Russian Messenger', '1866-01-01', '978-0486415873'),
('The Alchemist', 'Paulo', 'Coelho', 1988, 208, 'HarperCollins', '1988-05-01', '978-0062315007'),
('The Road', 'Cormac', 'McCarthy', 2006, 287, 'Alfred A. Knopf', '2006-09-26', '978-0307387899'),
('The Fault in Our Stars', 'John', 'Green', 2012, 313, 'Dutton Books', '2012-01-10', '978-0525478812'),
('The Hunger Games', 'Suzanne', 'Collins', 2008, 374, 'Scholastic Press', '2008-09-14', '978-0439023528'),
('Dune', 'Frank', 'Herbert', 1965, 412, 'Chilton Books', '1965-08-01', '978-0441013593');

INSERT INTO book_genres (book_id, genre_id) VALUES
(1, 3), (1, 9),
(2, 6), (2, 8),
(3, 1), (3, 4),
(4, 2), (4, 5),
(5, 1), (5, 7),
(6, 2), (6, 4),
(7, 1), (7, 6),
(8, 2), (8, 3),
(9, 6), (9, 7),
(10, 5), (10, 2),
(11, 3), (11, 9),
(12, 6), (12, 8),
(13, 1), (13, 4),
(14, 2), (14, 5),
(15, 1), (15, 7),
(16, 6), (16, 3),
(17, 5), (17, 8),
(18, 1), (18, 4),
(19, 1), (19, 6),
(20, 1), (20, 3);

INSERT INTO library_books (library_id, book_id) VALUES
(1, 1),(1, 1), (1, 1), (1, 1), (1, 1),
(1, 2), (1, 2), (1, 2), (1, 2), 
(1, 3), (1, 3), (1, 3),
(1, 4), (1, 4),
(1, 5), (1, 5), (1, 5), (1, 5), (1, 5),
(1, 6), (1, 6),
(1, 7),
(1, 8), (1, 8),
(1, 9), (1, 9), (1, 9), (1, 9), (1, 9),
(1, 10), (1, 10), (1, 10), (1, 10),
(2, 1), (2, 1),
(2, 2), (2, 2), (2, 2), (2, 2),
(2, 3), (2, 3), (2, 3), (2, 3), (2, 3),
(2, 4),
(2, 5), (2, 5), (2, 5),
(2, 6),
(2, 7), (2, 7), (2, 7),
(2, 8), (2, 8),
(3, 9), (3, 9),
(3, 10), (3, 10), (3, 10), (3, 10),
(3, 11),
(3, 12),
(3, 13), (3, 13), (3, 13),
(3, 14), (3, 14), (3, 14), (3, 14),
(3, 15), (3, 15),
(4, 16), (4, 16), (4, 16), (4, 16), (4, 16),
(4, 17), (4, 17), (4, 17),
(4, 18), (4, 18), (4, 18), (4, 18),
(4, 19), (4, 19),
(4, 20);

INSERT INTO customers 
(first_name, last_name, email_address, street_address, postcode, membership_start_date)
VALUES 
('Oliver', 'Smith', 'oliver.smith1985@gmail.com', '123 High Street', 'CV34 6PA', '2022-06-01'),
('Emily', 'Jones', 'emily.jones@outlook.com', '456 Church Road', 'CV35 7RL', '2021-07-15'),
('Charlotte', 'Brown', 'charlotte.brown@gmail.com', '789 Station Road', 'CV32 5AA', '2020-05-10'),
('Harry', 'Williams', 'harry.williams@yahoo.co.uk', '101 Queen Street', 'CV37 6AF', '2019-12-20'),
('Amelia', 'Taylor', 'amelia.taylor@live.co.uk', '202 Castle Lane', 'CV36 4AQ', '2023-08-05'),
('George', 'Davis', 'george.davis1990@gmail.com', '303 Park Avenue', 'CV34 7NP', '2023-03-25'),
('Isla', 'Miller', 'isla.miller@outlook.com', '404 Victoria Street', 'CV33 9BQ', '2022-10-30'),
('Jack', 'Wilson', 'jack.wilson@hotmail.com', '505 Elm Tree Road', 'CV35 9JE', '2023-09-10'),
('Sophie', 'Anderson', 'sophie.anderson123@gmail.com', '606 Willow Drive', 'CV32 5LG', '2020-01-15'),
('William', 'Thompson', 'william.thompson@yahoo.co.uk', '707 Pine Crescent', 'CV34 5UL', '2021-04-22'),
('Ella', 'White', 'ella.white@live.co.uk', '808 Maple Street', 'CV37 6HQ', '2020-11-05'),
('Alfie', 'Jackson', 'alfie.jackson1995@gmail.com', '909 Ash Road', 'CV35 8RT', '2022-02-14'),
('Mia', 'Harris', 'mia.harris@outlook.com', '123 Birch Lane', 'CV32 7HN', '2021-03-01'),
('Freddie', 'Martin', 'freddie.martin@yahoo.co.uk', '234 Cherry Avenue', 'CV33 9DL', '2019-01-28'),
('Lottie', 'Robinson', 'lottie.robinson@live.co.uk', '345 Maple Grove', 'CV34 8SF', '2021-05-17'),
('Theo', 'Thompson', 'theo.thompson1987@gmail.com', '456 Cedar Way', 'CV36 5QT', '2023-02-25'),
('Daisy', 'Smith', 'daisy.smith@outlook.com', '567 Spruce Court', 'CV37 9JG', '2022-08-20'),
('Henry', 'Hancock', 'henry.h@hotmail.com', '678 Poplar Place', 'CV35 4XS', '2021-07-01'),
('Grace', 'Clark', 'grace.clark1992@gmail.com', '789 Oak Avenue', 'CV34 5BQ', '2020-09-15'),
('Charlotte', 'Hall', 'charlotte.hall@yahoo.co.uk', '890 Elm Street', 'CV36 6RE', '2019-06-30'),
('James', 'Cooper', 'james.cooper1991@live.co.uk', '1010 Ash Drive', 'CV33 8WN', '2022-04-10');

INSERT INTO customer_loans (customer_id, book_id, library_id, loan_start_date, loan_due_date, return_date)
VALUES
(1, 1, 1, '2024-09-01', '2024-09-30', NULL), 
(2, 3, 1, '2024-08-20', '2024-09-20', '2024-09-19'), 
(3, 5, 2, '2024-07-10', '2024-08-10', '2024-08-05'), 
(4, 11, 3, '2024-09-15', '2024-10-15', NULL), 
(5, 7, 4, '2024-06-01', '2024-06-30', '2024-06-28'), 
(6, 9, 2, '2024-08-01', '2024-08-31', '2024-08-25'), 
(7, 4, 1, '2024-05-01', '2024-06-01', '2024-05-30'), 
(8, 6, 1, '2024-09-05', '2024-10-05', NULL), 
(9, 10, 3, '2024-04-25', '2024-05-25', '2024-05-24'), 
(10, 8, 4, '2024-02-10', '2024-03-10', '2024-03-08'), 
(11, 12, 3, '2024-08-20', '2024-09-20', '2024-09-19'), 
(12, 13, 2, '2024-03-15', '2024-04-15', '2024-04-10'), 
(13, 9, 1, '2024-09-01', '2024-09-30', NULL), 
(14, 16, 1, '2024-01-05', '2024-02-05', '2024-01-28'), 
(15, 18, 2, '2024-04-10', '2024-05-10', '2024-05-07'), 
(16, 20, 4, '2024-09-15', '2024-10-15', NULL), 
(17, 17, 2, '2024-05-25', '2024-06-25', '2024-06-22'), 
(18, 11, 3, '2024-03-20', '2024-04-20', '2024-04-18'), 
(19, 14, 2, '2024-06-10', '2024-07-10', '2024-07-05'), 
(20, 3, 1, '2024-08-01', '2024-09-01', NULL);
