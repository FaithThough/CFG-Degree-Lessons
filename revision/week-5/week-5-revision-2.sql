-- Creating a database
CREATE DATABASE employment;

USE employment;

-- Altering database to be read only
ALTER DATABASE employment READ ONLY = 1;

-- Database will not drop as it is in read only mode
DROP DATABASE employment;

-- Disabling read only mode
ALTER DATABASE employment READ ONLY = 0;

-- Creating a table
CREATE TABLE employees (
	employee_id INT,
    first_name VARCHAR (50),
    last_name VARCHAR (50),
    hourly_pay DECIMAL(5,2),
    hire_date DATE
);

-- Selecting everything from table
SELECT * FROM employees;

-- Adding a column to a table
ALTER TABLE employees
ADD phone_number VARCHAR(15);

-- Changing a column name in a table
ALTER TABLE employees
RENAME COLUMN phone_number TO email;

-- Changing a data type of a column in a table
ALTER TABLE employees
MODIFY COLUMN email VARCHAR(100);

-- Moving a column to a different position in a table
ALTER TABLE employees
MODIFY email VARCHAR(100)
AFTER last_name;

SELECT * FROM employees;

-- Removing a column from a table
ALTER TABLE employees
DROP COLUMN email;

-- Inserting a row into a table
INSERT INTO employees
VALUES (
	1, "Eugene", "Krabs", 25.50, "2023-01-02"
);

-- Inserting multiple rows into a table
INSERT INTO employees VALUES
(2, "Squidward", "Tentacles", 15.00, "2023-01-03"),
(3, "SpongeBob", "SquarePants", 12.50, "2023-01-04"),
(4, "Patrick", "Star", 12.50, "2023-01-05"),
(5, "Sandy", "Cheeks", 17.25, "2023-01-06");

-- Inserting a row with missing data
INSERT INTO employees (employee_id, first_name, last_name) VALUES
(6, "Sheldon", "Plankton");

-- Selecting all columns and all rows from a table
SELECT * FROM employees;

-- Selecting just the first and last names from the table
SELECT first_name, last_name 
FROM employees;

-- Where clause
SELECT * 
FROM employees
WHERE employee_id = 1;

SELECT * 
FROM employees
WHERE first_name = "SpongeBob";

SELECT * 
FROM employees
WHERE hourly_pay >= 15;

SELECT * 
FROM employees
WHERE hire_date <= "2023-01-03";

-- Not comparison operator !=
SELECT * 
FROM employees
WHERE employee_id != 1;

-- NULL
SELECT * FROM employees
WHERE hire_date IS NULL;

-- Updating a row in a table
UPDATE employees
SET hourly_pay = 10.50, 
	hire_date = NULL
WHERE employee_id = 6;

SELECT * 
FROM employees 
WHERE employee_id = 6;

-- Deleting a row from a table
DELETE FROM employees
WHERE employee_id = 6;

SELECT * FROM employees;

-- CURRENT_DATE() & CURRENT_TIME
CREATE TABLE clock_in(
 clock_in_date DATE,
 clock_in_time TIME,
 clock_in_date_time DATETIME
);

SELECT * FROM clock_in;

INSERT INTO clock_in
VALUES (CURRENT_DATE(), CURRENT_TIME(), NOW());

SELECT * FROM clock_in;

DROP TABLE clock_in;

-- UNIQUE constraint

CREATE TABLE products (
	product_id INT,
    product_name VARCHAR(25) UNIQUE,
    price DECIMAL(4, 2)
);

SELECT * FROM products;

INSERT INTO products 
VALUES 
		(1, "Hamburger", 3.99),
		(2, "Fries", 1.89),
		(3, "Soda", 1.00),
		(4, "Ice cream", 1.49);
        
-- NOT NULL constraint

ALTER TABLE products 
MODIFY price DECIMAL(4,2) NOT NULL;

INSERT INTO products
VALUES
	(5, "Cookie", 0);
    
-- CHECK constraint
ALTER TABLE employees
ADD CONSTRAINT chk_hourly_pay CHECK(hourly_pay >= 10.00);

SELECT * FROM employees;

INSERT INTO employees 
VALUES (6, "Pearl", "Krabs", 10.00, "2023-01-07");

-- Deleting a CHECK constraint
ALTER TABLE employees
DROP CHECK chk_hourly_pay;

-- DEFAULT constraint
SELECT * FROM products;

UPDATE products
SET product_name = "straw"
WHERE product_id = 5; 

INSERT INTO products
VALUES 
		(6, "Napkin", 0.00), 
		(7, "Fork", 0.00),
        (8, "Spoon", 0.00);
        
DELETE FROM products
WHERE product_id >= 5;

SELECT * FROM products;

ALTER TABLE products
ALTER price SET DEFAULT 0;

INSERT INTO products (product_id, product_name)
VALUES 
		(5, "Straw"),
		(6, "Napkin"), 
		(7, "Fork"),
        (8, "Spoon");
        
CREATE TABLE transactions(
	transaction_id INT,
    amount DECIMAL (5,2),
    transaction_date DATETIME DEFAULT NOW()
    );
    
SELECT * FROM transactions;

INSERT INTO transactions (transaction_id, amount)
VALUES 
	(3, 8.37);
    
DROP TABLE transactions;

-- PRIMARY KEY constraint
-- New table
CREATE TABLE transactions(
	transaction_id INT PRIMARY KEY,
    amount DECIMAL (5,2)
);

SELECT * FROM transactions;

-- Existing table
ALTER TABLE employees
ADD CONSTRAINT
PRIMARY KEY(employee_id);

SELECT * FROM employees;

-- Testing the limit of one primary key per table
ALTER TABLE employees
ADD CONSTRAINT
PRIMARY KEY(hourly_pay);

SELECT * FROM transactions;

INSERT INTO TRANSACTIONS
VALUES (1003, 4.49);

SELECT amount
FROM transactions
WHERE transaction_id = 1001;

-- AUTO_INCREMENT
DROP TABLE transactions; 

CREATE TABLE transactions (
	transaction_id INT PRIMARY KEY AUTO_INCREMENT,
    amount DECIMAL (5,2)
);

INSERT INTO transactions (amount)
VALUES (4.99);

SELECT * FROM transactions;

ALTER TABLE transactions
AUTO_INCREMENT = 1000;

DELETE FROM transactions;

INSERT INTO transactions (amount)
VALUES (4.99),
		(2.89),
        (3.38),
        (4.99);
        
SELECT * FROM transactions;

CREATE TABLE customers (
	customer_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR (50),
    last_name VARCHAR (50)
);

INSERT INTO customers (first_name, last_name)
VALUES ("Larry", "Lobster"),
		("Bubble", "Bass"),
        ("Mrs", "Puff"),
        ("Mermaid", "Man"),
        ("Barnacle", "Boy");
        
SELECT * FROM customers;

DROP TABLE transactions;

CREATE TABLE transactions (
	transaction_id INT PRIMARY KEY AUTO_INCREMENT,
    amount DECIMAL (5,2),
    customer_id INT, 
    FOREIGN KEY(customer_id) REFERENCES customers(customer_id)
);

SELECT * FROM transactions;


        
		
