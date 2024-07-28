-- Let's create a very simple sample bank account database
CREATE DATABASE bank;

-- Use the newly created database
USE bank;

-- Create a table for accounts
CREATE TABLE accounts (
  account_number INT(11) DEFAULT NULL,
  account_holder_name VARCHAR(50) DEFAULT NULL,
  account_holder_surname VARCHAR(50) DEFAULT NULL,
  balance FLOAT DEFAULT NULL,
  overdraft_allowed TINYINT(1) DEFAULT NULL
);

-- Insert sample data into the accounts table
INSERT INTO accounts
(account_number, account_holder_name, account_holder_surname, balance, overdraft_allowed)
VALUES
(111112, 'Julie', 'Smith', 150, true),
(111113, 'James', 'Andrews', 20, false),
(111114, 'Jack', 'Oakes', -70, true),
(111115, 'Jasper', 'Wolf', 200, true);

-- Select all records from the accounts table
SELECT * FROM accounts;

START TRANSACTION;
SELECT 
	@money_availible:= IF(balance > 0, balance, 0) AS money_availible
FROM accounts
WHERE account_number = 111112 AND account_holder_surname = 'Smith';

SET @transfer_amount = 50;

UPDATE accounts 
SET 
	balance = balance - @transfer_amount
WHERE
	account_number = 111112 AND account_holder_surname = 'Smith';

SELECT account_number, account_holder_name, account_holder_surname, balance FROM accounts 
WHERE account_number = 111112;
    
-- Declaring a variable
SET @name = "Faith";
SET @name := "Marcus";
SELECT @name AS name;

-- Control flow
SET @age := 12;
SELECT
    CASE
        WHEN @age < 18 THEN "You need your parents' permission"
        WHEN @age >= 18 THEN "Permission is not required"
        ELSE "Not valid"
    END AS message;
    
SELECT IF (1>2, 'yes', 'no') AS result;

SELECT IFNULL(NULL, 0);

