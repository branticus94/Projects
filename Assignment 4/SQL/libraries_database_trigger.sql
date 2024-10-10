USE libraries_database;

DELIMITER //

CREATE TRIGGER set_loan_due_date
BEFORE INSERT ON customer_loans
FOR EACH ROW
BEGIN
    -- Set loan_due_date to 1 month after loan_start_date
    SET NEW.loan_due_date = DATE_ADD(NEW.loan_start_date, INTERVAL 1 MONTH);
END //

DELIMITER ;