-- Scenario of use:
-- I want to create a system for a car rental buisness to manage their cars, customers, availalable equipment (car seat, gps, high-vis jacket) and rentals.

-- Environment SetUp (Creating database etc)
-- Creating a database to manage the car rental system with at least 3 tables with several columns, using good naming conventions
CREATE DATABASE IF NOT EXISTS Car_Rental_Management_Database;

USE Car_Rental_Management_Database;

-- Schema Definitions
CREATE TABLE IF NOT EXISTS Cars (
    car_id INT AUTO_INCREMENT PRIMARY KEY,
    make VARCHAR(50) NOT NULL,
    model VARCHAR(50) NOT NULL,
    year YEAR NOT NULL,
    price_per_day DECIMAL(8 , 2 ) NOT NULL CHECK (price_per_day > 0.00),
    fuel_type VARCHAR(20),
    mileage INT CHECK (mileage >= 0),
    car_type VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS Car_Rental_Equipment (
    equipment_id INT AUTO_INCREMENT PRIMARY KEY,
    equipment_name VARCHAR(50) NOT NULL,
    item_count INT NOT NULL
);

CREATE TABLE IF NOT EXISTS Customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    surname VARCHAR(100) NOT NULL,
    phone VARCHAR(11),
    email VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS Car_Rentals (
    car_rental_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    car_id INT,
    rental_start_date DATE NOT NULL,
    rental_end_date DATE NOT NULL,
    FOREIGN KEY (car_id)
        REFERENCES Cars (car_id)
);

CREATE TABLE Equipment_Rentals (
    equipment_rental_id INT AUTO_INCREMENT PRIMARY KEY,
    item_id INT,
    car_rental_id INT,
    FOREIGN KEY (item_id)
        REFERENCES Car_Rental_Equipment (equipment_id),
    FOREIGN KEY (car_rental_id)
        REFERENCES Car_Rentals (car_rental_id)
);

-- Functions
-- I need to create a function which works out if a car is available for rental using the following logic:
		-- |            |starts before|starts between|starts after|
        -- |ends before |       0     |      2       |      2     |
        -- |ends between|       1     |      1       |      2     |
        -- |ends after  |       1     |      1       |      0     |
        -- 0 means the car is available, 1 means that the car is unavailable and 2 means the condition cannot exist logically
        -- As you can see in order to be available the rental must start and end before the selected date or after the selected date
        
DELIMITER //
CREATE FUNCTION check_car_available (requested_start_date DATE, requested_end_date DATE, start_date DATE, end_date DATE)
RETURNS BOOLEAN
DETERMINISTIC
BEGIN
	DECLARE is_available BOOLEAN;
    
    IF start_date < requested_start_date AND end_date < requested_start_date THEN
		SET is_available = true;
    ELSEIF start_date > requested_end_date AND end_date > requested_end_date THEN
		SET is_available = true;
	ELSE
		SET is_available = false;
	END IF;
    RETURN is_available;
END//
DELIMITER ;	

DELIMITER //
CREATE FUNCTION Calculate_Rental_Duration(
    rental_start_date DATE, 
    rental_end_date DATE)
RETURNS INT
DETERMINISTIC
BEGIN
    RETURN DATEDIFF(rental_end_date, rental_start_date);
END //
DELIMITER ;

DELIMITER //
CREATE FUNCTION Calculate_Total_Rental_Price(rental_id INT)
RETURNS DECIMAL(10,2)
DETERMINISTIC
BEGIN
    DECLARE car_price_per_day DECIMAL(10,2);
    DECLARE rental_days INT;
    DECLARE equipment_total_price DECIMAL(10,2);
    DECLARE total_price DECIMAL(10,2);

    SET equipment_total_price = 0;

    SELECT 
        c.price_per_day,
        cr.rental_start_date,
        cr.rental_end_date
    INTO 
        car_price_per_day, @start_date, @end_date
    FROM 
        Car_Rentals cr
    JOIN 
        Cars c ON cr.car_id = c.car_id
    WHERE 
        cr.car_rental_id = rental_id;

    -- Use the function to calculate the rental duration (in days)
    SET rental_days = calculate_rental_duration(@start_date, @end_date);

    -- Calculate the total price for the car rental
    SET total_price = car_price_per_day * rental_days;

    -- Calculate the total price for the rented equipment (assuming a fixed price of £5 per item per day)
    SELECT 
        COUNT(*) * 5 * rental_days 
    INTO 
        equipment_total_price
    FROM 
        Equipment_Rentals er
    WHERE 
        er.car_rental_id = rental_id;

    -- Add the equipment price to the total rental price
    SET total_price = total_price + equipment_total_price;

    RETURN total_price;
END //
DELIMITER ;

-- Stored Procedures
DELIMITER //
CREATE PROCEDURE Add_Car_Rental(
    IN customer_id INT, 
    IN car_id INT, 
    IN rental_start_date DATE, 
    IN rental_end_date DATE)
BEGIN
    DECLARE is_available BOOLEAN;
    
    -- Check if the car is available for the requested dates
	SET is_available = NOT EXISTS (
		SELECT 1
		FROM Car_Rentals cr
		WHERE cr.car_id = car_id
			AND check_car_available(rental_start_date, rental_end_date, cr.rental_start_date, cr.rental_end_date) = 0);
    
    IF is_available THEN
        INSERT INTO Car_Rentals(customer_id, car_id, rental_start_date, rental_end_date)
        VALUES (customer_id, car_id, rental_start_date, rental_end_date);
        SELECT "Rental successfully added.";
    ELSE
        SELECT "Car is unavailable for the selected dates.";
    END IF;
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE Return_Car(
    IN car_rental_id INT, 
    IN new_mileage INT)
BEGIN
    UPDATE Cars c
    INNER JOIN Car_Rentals r ON c.car_id = r.car_id
    SET c.mileage = new_mileage
    WHERE r.car_rental_id = car_rental_id;
    SELECT "Car returned and mileage updated.";
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE Calculate_Total_Rental_Price(IN rental_id INT, OUT total_price DECIMAL(10,2))
BEGIN
    DECLARE car_price_per_day DECIMAL(10,2);
    DECLARE rental_days INT;
    DECLARE equipment_total_price DECIMAL(10,2);

    -- Set equipment price to 0
    SET equipment_total_price = 0;

    -- Get the price per day for the car and rental start/end dates
    SELECT 
        c.price_per_day,
        cr.rental_start_date,
        cr.rental_end_date
    INTO 
        car_price_per_day, @start_date, @end_date
    FROM 
        Car_Rentals cr
    JOIN 
        Cars c ON cr.car_id = c.car_id
    WHERE 
        cr.car_rental_id = rental_id;

    -- Use the function to calculate the rental duration (in days)
    SET rental_days = calculate_rental_duration(@start_date, @end_date);

    SET total_price = car_price_per_day * rental_days;

    -- Calculate the total price for the rented equipment (assuming a fixed price of £5 per item per day)
    SELECT 
        COUNT(*) * 5 * rental_days 
    INTO 
        equipment_total_price
    FROM 
        Equipment_Rentals er
    WHERE 
        er.car_rental_id = rental_id;

    -- Add the equipment price to the total rental price
    SET total_price = total_price + equipment_total_price;
END//
DELIMITER ;

-- Triggers
-- Here I have made a trigger which fires before an equipment rental is inserted - if the equipment is not available an error is thrown, 
-- it relies upon the vw_Available_Equipment view - therefore please uncomment and run once the rest of the code has run

-- DELIMITER //
-- CREATE TRIGGER before_insert_equipment_rental
-- BEFORE INSERT ON Equipment_Rentals
-- FOR EACH ROW
-- BEGIN
--     DECLARE available_stock INT;
--     SELECT Available INTO available_stock
--     FROM vw_Available_Equipment
--     WHERE equipment_id = NEW.item_id;
--     IF available_stock <= 0 THEN
--         SIGNAL SQLSTATE '45000'
--         SET MESSAGE_TEXT = 'Error: The requested equipment is out of stock.';
--     END IF;
-- END;
-- //
-- DELIMITER ;

-- Data Manipulation (Inserts etc.)
-- Here I populate the database with at least 8 rows of mock data per table to show use of DML commands.

-- DML (Data Manipulation Language) commands in SQL are used to manage and manipulate data within a database. The primary DML commands include:
-- SELECT: Retrieves data from one or more tables. It can include various clauses to filter, sort, and aggregate the data.
-- INSERT: Adds new rows of data to a table.
-- UPDATE: Modifies existing data in a table. It can change one or multiple columns based on specified conditions.
-- DELETE: Removes one or more rows from a table based on specified conditions.

INSERT INTO Cars 
(make, model, year, price_per_day, fuel_type, mileage, car_type)
VALUES
('Toyota', 'Yaris', '2021', 30.00, 'Petrol', 12000, 'Hatchback'),
('Skoda', 'Octavia', '2020', 40.00, 'Diesel', 22000, 'Saloon'),
('Peugeot', '3008', '2022', 55.00, 'Diesel', 5000, 'SUV'),
('Volvo', 'XC60', '2021', 70.00, 'Hybrid', 8000, 'SUV'),
('Mini', 'Cooper', '2019', 45.00, 'Petrol', 18000, 'Hatchback'),
('Land Rover', 'Discovery', '2020', 90.00, 'Diesel', 15000, 'SUV'),
('Mazda', 'MX-5', '2022', 75.00, 'Petrol', 3000, 'Convertible'),
('Hyundai', 'i30', '2021', 33.00, 'Petrol', 16000, 'Hatchback'),
('Citroen', 'C4', '2019', 35.00, 'Diesel', 24000, 'Hatchback'),
('Ford', 'Puma', '2020', 50.00, 'Petrol', 20000, 'SUV'),
('Vauxhall', 'Astra', '2020', 35.50, 'Petrol', 15000, 'Hatchback'),
('Ford', 'Fiesta', '2019', 28.00, 'Diesel', 22000, 'Hatchback'),
('BMW', '3 Series', '2021', 55.75, 'Petrol', 18000, 'Saloon'),
('Tesla', 'Model 3', '2022', 85.00, 'Electric', 12000, 'Saloon'),
('Audi', 'A4', '2018', 45.00, 'Diesel', 30000, 'Saloon'),
('Volkswagen', 'Golf', '2019', 32.25, 'Petrol', 25000, 'Hatchback'),
('Mercedes', 'C-Class', '2021', 60.00, 'Hybrid', 14000, 'Saloon'),
('Honda', 'Civic', '2020', 33.75, 'Petrol', 17000, 'Hatchback'),
('Nissan', 'Qashqai', '2017', 40.00, 'Diesel', 40000, 'SUV'),
('Kia', 'Sportage', '2018', 38.50, 'Petrol', 33000, 'SUV'),
('Ford', 'Mustang', '2024', 100.00, 'Petrol', 0, 'Coupe'),
('Tesla', 'Model Y', '2024', 90.00, 'Electric', 0, 'SUV'),
('Vauxhall', 'Corsa', '2023', 70.00, 'Petrol', 800, 'Hatchback');

INSERT INTO Car_Rental_Equipment 
(equipment_name, item_count)
VALUES
('Sat Nav', 5),
('Child Seat', 10),
('Cleaning Kit', 10),
('Roof Box', 5),
('Portable Car Fridge', 3),
('Tyre Pressure Gauge', 10),
('First Aid Kit', 20),
('Ice Scraper', 20),
('High-Visibility Vest', 10),
('Breakdown Kit', 5);

INSERT INTO Customers 
(first_name, surname, phone, email)
VALUES
('Lily', 'Wilkins', '07189012345', 'lily.wilkins@gmail.com'),
('Amelia', 'Johnson', '07198765432', 'amelia.johnson@outlook.com'),
('Isabella', 'Jones', '07145678901', 'isabella.jones@hotmail.co.uk'),
('Harry', 'Moore', '07190123456', 'harry.moore@gmail.com'),
('Emily', 'Tate', '07101234567', 'emily.tate@outlook.com'),
('Benjamin', 'Harris', '07156789013', 'benjamin.harris@hotmail.co.uk'),
('Sophie', 'Walker', '07101234578', 'sophie.walker@gmail.com'),
('James', 'Anderson', '07112345678', 'james.anderson@outlook.com'),
('Mia', 'Lewis', '07189012356', 'mia.lewis@hotmail.co.uk'),
('Charlie', 'Williams', '07134567890', 'charlie.williams@gmail.com'),
('Alfie', 'Lee', '07190123467', 'alfie.lee@outlook.com'),
('Poppy', 'Clarkson', '07167890134', 'poppy.clarkson@hotmail.co.uk'),
('George', 'Brownlow', '07156789012', Null),
('Freddie', 'Hughes', '07178901245', 'freddie.hughes@outlook.com'),
('Chloe', 'Thompson', '07123456780', 'chloe.thompson@hotmail.co.uk'),
('Oliver', 'Smithson', '07123456789', 'oliver.smithson@gmail.com'),
('Samuel', 'Jackson', '07134567891', 'samuel.jackson@outlook.com'),
('Sophia', 'Davis', '07167890123', 'sophia.davis@hotmail.co.uk'),
('Ella', 'Whitehead', '07145678902', Null),
('Jack', 'Miller', '07178901234', 'jack.miller@outlook.com'),
('Lucas', 'Bennett', '07123456701', 'lucas.bennett@gmail.com'),
('Sophie', 'Harrison', '07123456702', 'sophia.harrison@outlook.com'),
('Ella', 'Barker', '07123456703', Null),
('Noah', 'Mitchell', '07123456704', 'noah.mitchell@gmail.com'),
('Ava', 'Fletcher', '07123456705', 'ava.fletcher@outlook.com');

-- Ella Barker now wants to provide an email address I use the UPDATE function as per the following query: 
UPDATE Customers
SET email = 'ella.barker@gmail.com'
WHERE customer_id = 23;

-- As you can see the database is now updated:
Select * FROM Customers;

INSERT INTO Car_Rentals (customer_id, car_id, rental_start_date, rental_end_date)
VALUES
(3, 5, '2024-09-01', '2024-09-14'),
(2, 15, '2024-08-15', '2024-09-05'),
(3, 4, '2024-07-10', '2024-07-20'),
(4, 17, '2024-09-02', '2024-09-09'),
(5, 3, '2024-06-01', '2024-06-15'),
(6, 1, '2024-05-25', '2024-06-05'),
(7, 2, '2024-04-15', '2024-04-20'),
(15, 3, '2024-09-03', '2024-09-17'),
(9, 18, '2024-08-01', '2024-08-10'),
(10, 14, '2024-07-05', '2024-07-15'),
(11, 7, '2024-08-15', '2024-08-20'),
(16, 6, '2024-09-04', '2024-09-18'),
(13, 11, '2024-09-05', '2024-09-10'),
(14, 8, '2024-09-06', '2024-09-12'),
(15, 5, '2024-01-15', '2024-01-25'),
(16, 4, '2024-03-01', '2024-03-15'),
(17, 3, '2024-02-20', '2024-02-27'),
(18, 16, '2024-08-20', '2024-08-25'),
(19, 20, '2024-09-07', '2024-09-30'),
(20, 10, '2024-09-29', '2024-10-02'),
(1, 19, '2024-09-09', '2024-09-16'),
(2, 10, '2024-05-10', '2024-05-15'),
(3, 2, '2024-06-20', '2024-06-30'),
(5, 1, '2024-09-11', '2024-09-25'),
(5, 15, '2024-02-15', '2024-02-20'),
(6, 9, '2024-01-01', '2024-01-10'),
(7, 18, '2024-03-20', '2024-03-23'),
(8, 13, '2024-09-12', '2024-09-16'),
(9, 12, '2024-09-13', '2024-09-14'),
(10, 2, '2024-10-01', '2024-10-05'),
(11, 7, '2024-10-10', '2024-10-15'),
(12, 10, '2024-10-20', '2024-10-25'),
(13, 8, '2024-10-05', '2024-10-25'),
(14, 15, '2024-10-15', '2024-10-20');

INSERT INTO Equipment_Rentals (item_id, car_rental_id)
VALUES
(1, 1),
(2, 1),
(3, 2),
(4, 3),
(5, 4),
(1, 5),
(6, 6),
(7, 7),
(8, 8),
(2, 9),
(3, 10),
(9, 11),
(10, 12),
(4, 13),
(5, 14),
(6, 15),
(7, 16),
(8, 17),
(1, 18),
(9, 19),
(10, 20);

-- Queries for Testing

-- Here I present 5 queries to retrieve data, using data sorting for majority of queries with ORDER BY:

-- Query 1
-- The following query identifies which cars are £40 or less per day ordering price most to least expensive
CREATE VIEW vw_Cars_Less_Than_40 AS
SELECT 
    c.make AS 'Make',
    c.model AS 'Model',
    c.price_per_day AS 'Price Per Day (£)'
FROM
    Cars c
WHERE
    price_per_day <= 40
ORDER BY c.price_per_day DESC;

SELECT * FROM vw_Cars_Less_Than_40;

-- Query 2
-- The following query identifies which SUV or saloon cars are available for rental over the next 7 days ordering by lowest to highest mileage
CREATE VIEW vw_Suv_Saloon_Cars_Available AS
SELECT 
    CONCAT(c.make, ' ', c.model) AS 'Available Car', car_type as 'Car Type', mileage as "Mileage"
FROM
    cars c
WHERE
    car_id NOT IN (SELECT 
            cr.car_id
        FROM
            Car_Rentals cr
        WHERE
            CHECK_CAR_AVAILABLE(CURDATE(),
                    CURDATE() + INTERVAL 7 DAY,
                    cr.rental_start_date,
                    cr.rental_end_date) = 0)
        AND car_type IN ('Saloon' , 'SUV')
ORDER BY mileage;

SELECT * FROM vw_Suv_Saloon_Cars_Available;

-- I could also achieve this with a union - uncomment to run
-- SELECT 
--     CONCAT(c.make, ' ', c.model) AS 'Available Car', car_type as 'Car Type', mileage as "Mileage"
-- FROM
--     cars c
-- WHERE
--     car_id NOT IN (SELECT 
--             cr.car_id
--         FROM
--             Car_Rentals cr
--         WHERE
--             CHECK_CAR_AVAILABLE(CURDATE(),
--                     CURDATE() + INTERVAL 7 DAY,
--                     cr.rental_start_date,
--                     cr.rental_end_date) = 0)
--         AND car_type = 'Saloon'
-- UNION
-- SELECT 
--     CONCAT(c.make, ' ', c.model) AS 'Available Car', car_type as 'Car Type', mileage as "Mileage"
-- FROM
--     cars c
-- WHERE
--     car_id NOT IN (SELECT 
--             cr.car_id
--         FROM
--             Car_Rentals cr
--         WHERE
--             CHECK_CAR_AVAILABLE(CURDATE(),
--                     CURDATE() + INTERVAL 7 DAY,
--                     cr.rental_start_date,
--                     cr.rental_end_date) = 0)
--         AND car_type = 'SUV'
-- 	ORDER BY Mileage;
        
-- Query 3
-- I want to see which customers have signed up but are yet to rent a car so that I can target advertising towards them
CREATE VIEW vw_Target_Advertisement AS
SELECT 
    cust.first_name, cust.surname, cust.phone, cust.email
FROM
    Customers cust
        LEFT JOIN
    Car_Rentals cr ON cust.customer_id = cr.customer_id
WHERE
    cr.car_rental_id IS NULL;
    
SELECT * FROM vw_Target_Advertisement;

-- Query 4
-- I want to offer a discount on future rentals to customers who have used our buisness three or more times I can perform the following query:
CREATE VIEW vw_Customer_Loyalty AS
SELECT 
    c.customer_id AS 'Customer ID',
    c.first_name AS 'First Name',
    c.surname AS 'Surname',
    (SELECT 
            COUNT(*)
        FROM
            Car_Rentals cr
        WHERE
            cr.customer_id = c.customer_id) AS Count
FROM
    Customers c
HAVING Count >= 3;

SELECT * FROM vw_Customer_Loyalty;

-- Query 5
-- I want to see the current stock of the rental equipment, ordered by id; I have created a view so that this can be called quickly
CREATE VIEW vw_Available_Equipment AS
SELECT 
    cre.equipment_id,
    cre.equipment_name AS 'Equipment Name', 
    cre.item_count AS 'Total Stock', 
    COALESCE(Rented_Items.rented_out, '0')  AS 'Rented Out',
    (cre.item_count - COALESCE(Rented_Items.rented_out, '0')) AS Available
FROM
    Car_Rental_Equipment cre
        LEFT JOIN
    (SELECT 
        item_id, COUNT(item_id) AS rented_out
    FROM
        Equipment_Rentals
    WHERE
        car_rental_id IN (SELECT 
                car_rental_id
            FROM
                Car_Rentals cr
            WHERE
                CHECK_CAR_AVAILABLE(CURDATE(), CURDATE(), cr.rental_start_date, cr.rental_end_date) = 0)
    GROUP BY item_id) AS Rented_Items ON Rented_Items.item_id = equipment_id
    ORDER BY cre.equipment_name;

SELECT * FROM vw_Available_Equipment ORDER BY equipment_id;

-- Use at least 1 query to delete data
-- Car 23 has a fault and needs to be scrapped so delete the car as follows
DELETE FROM Cars 
WHERE
    Cars.car_id = 23;

-- Aggregate functions in SQL are special functions that perform calculations on a set of values and return a single value. 
-- They are often used in conjunction with the GROUP BY clause to summarize data. 
-- Here are some commonly used aggregate functions:
-- Here I use COUNT() to return a summary of the car stock by type of car, excluding convirtible cars, ordering by fewest number of cars to greatest.
CREATE VIEW vw_Car_Stock AS
SELECT 
    c.car_type AS 'Car Type', COUNT(car_type) AS 'Number of Cars'
FROM
    Cars c
GROUP BY c.car_type
HAVING c.car_type != 'Convertible'
ORDER BY COUNT(c.car_type);

SELECT * FROM vw_Car_Stock;

-- Here I use AVG() to calculate the average price per day of each car type I also use the round in-built function to show the price to two decimal places
CREATE VIEW vw_Average_Price_Car_Type AS
SELECT 
    c.car_type AS 'Car Type', ROUND(AVG(price_per_day), 2) AS 'Average Price Per Day'
FROM
    Cars c
GROUP BY c.car_type
ORDER BY AVG(price_per_day);

SELECT * FROM vw_Average_Price_Car_Type;

-- Here I use MAX() to return the most expensive car.
CREATE VIEW vw_Most_Expensive_Car AS
SELECT CONCAT(make, " ", model) AS 'Most Expensive Car',
       CONCAT("£", price_per_day) AS 'Price'
FROM Cars
WHERE price_per_day = (SELECT MAX(price_per_day) FROM Cars);

SELECT * FROM vw_Most_Expensive_Car;

-- Here I use MIN() to return the least expensive car.
CREATE VIEW vw_Least_Expensive_Car AS
SELECT CONCAT(make, " ", model) AS 'Least Expensive Car',
       CONCAT("£", price_per_day) AS 'Price'
FROM Cars
WHERE price_per_day = (SELECT MIN(price_per_day) FROM Cars);

SELECT * FROM vw_Least_Expensive_Car;

-- Use at least 2 joins
-- Here I use a right join to join the car information to the rental start and end date
CREATE VIEW vw_Right_Join_Car_Rental_Start_And_End AS
SELECT CONCAT(c.make, " ", c.model) AS 'Car', cr.rental_start_date AS 'Rental Start Date', cr.rental_end_date AS 'Rental End Date'
FROM Cars c
RIGHT JOIN Car_Rentals cr
ON c.car_id=cr.car_id
ORDER BY cr.rental_start_date;

SELECT * FROM vw_Right_Join_Car_Rental_Start_And_End;

-- Here I use a left join to display the items associated with a specific car rental id
CREATE VIEW vw_Left_Join_Car_Rental_Equipment AS 
SELECT car_rental_id AS 'Car Rental ID', equipment_name AS 'Equipment'
FROM Equipment_Rentals er
LEFT JOIN Car_Rental_Equipment cre
ON item_id = cre.equipment_id;

SELECT * FROM vw_Left_Join_Car_Rental_Equipment;

-- Use at least 2 additional in-built functions (to the two aggregate functions already counted in previous point)
-- Here I use the date format function to format the year and month for my summary of revenue
CREATE VIEW vw_Revenue_Summary AS 
SELECT 
    DATE_FORMAT(cr.rental_start_date, '%Y-%m') AS "Rental Month",
    SUM(Calculate_Total_Rental_Price(cr.car_rental_id)) AS "Total Revenue" 
FROM 
    Car_Rentals cr
JOIN 
    Cars c ON cr.car_id = c.car_id
GROUP BY 
    DATE_FORMAT(cr.rental_start_date, '%Y-%m')
ORDER BY 
    DATE_FORMAT(cr.rental_start_date, '%Y-%m');
    
SELECT * FROM vw_Revenue_Summary;

-- Here I use the concat function to combine the make and model of the car to summarise the total number of 
-- rentals for each car, ordering by most to fewest rentals
CREATE VIEW vw_Rentals_Per_Car AS 
SELECT 
    CONCAT(c.make, ' ', c.model) AS Car,
    COUNT(cr.car_rental_id) AS "Total Rentals"
FROM 
    Cars c
LEFT JOIN 
    Car_Rentals cr ON c.car_id = cr.car_id
GROUP BY 
    c.car_id
ORDER BY 
    COUNT(cr.car_rental_id) DESC; 
    
SELECT * FROM vw_Rentals_Per_Car;

-- Clean-up (if required)
-- DROP DATABASE Car_Rental_Management_Database;