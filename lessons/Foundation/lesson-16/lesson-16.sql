CREATE DATABASE ecomerce;
USE ecomerce;

CREATE TABLE CUSTOMERS(
CUSTOMER_ID INTEGER PRIMARY KEY auto_increment,
CUSTOMER_NAME VARCHAR(50) NOT NULL,
PHONE INTEGER,
EMAIL_ADDRESS VARCHAR(50) UNIQUE
);

CREATE TABLE ORDERS(
ORDER_ID INTEGER PRIMARY KEY auto_increment,
ORDER_STATUS enum('Processed','Dispatched','Delivered') NOT NULL,
TOTAL_AMOUNT INTEGER, 
QUANTITY INTEGER,
CUSTOMER_ID INTEGER,
CONSTRAINT FK_CUSTOMERORDER FOREIGN KEY(CUSTOMER_ID)
REFERENCES CUSTOMERS(CUSTOMER_ID)
);

-- No need of ID as its auto-increment
INSERT INTO CUSTOMERS (CUSTOMER_NAME, PHONE, EMAIL_ADDRESS)
 VALUES 
('Amelia', 75872981, 'ame@hotmail.com'),
('Daisy', 12345678, 'daisy@example.com'),
('Marine', 87654321, 'marine@example.com'),
('Nuala', 23456789, 'nuala@example.com'),
('Sophie', 98765432, 'sophie@example.com');

INSERT INTO ORDERS (ORDER_STATUS, TOTAL_AMOUNT, QUANTITY, CUSTOMER_ID)
VALUES 
('Dispatched', 10, 2, 1),  -- Amelia
('Processed', 20, 1, 1),   -- Amelia
('Delivered', 15, 3, 2),   -- Daisy
('Processed', 30, 4, 3),   -- Marine
('Dispatched', 25, 5, 4);  -- Nuala

INSERT INTO ORDERS (ORDER_STATUS, TOTAL_AMOUNT, QUANTITY, CUSTOMER_ID)
VALUES 
('Dispatched', 10, 2, 6);

-- Delete FK before deleting the table otherwise it will show an error
ALTER TABLE ORDERS
DROP CONSTRAINT FK_CUSTOMERORDER;

-- Deleting just records from tables
DELETE from ORDERS;
DELETE from CUSTOMERS;

DROP TABLE ORDERS;

-- To delete the table record and also to reset the ID (auto-increment)
TRUNCATE table CUSTOMERS;
TRUNCATE table ORDERS;

-- view the table records
SELECT * FROM CUSTOMERS;
SELECT * FROM ORDERS;



-- Inner Join
-- Retrieve a list of all customers and their respective orders. 
-- Only show customers who have placed an order.
-- Inner Join: Retrieve customers who have placed orders
SELECT
	CUSTOMERS.CUSTOMER_NAME,
    CUSTOMERS.EMAIL_ADDRESS,
    ORDERS.ORDER_STATUS,
    ORDERS.TOTAL_AMOUNT
FROM CUSTOMERS
INNER JOIN
	ORDERS
ON
	CUSTOMERS.CUSTOMER_ID = ORDERS.CUSTOMER_ID;

-- Left Join
-- Retrieve a list of all customers and their orders, including customers who have not placed any orders.
SELECT
	CUSTOMERS.CUSTOMER_NAME,
    CUSTOMERS.EMAIL_ADDRESS,
    ORDERS.ORDER_STATUS,
    ORDERS.TOTAL_AMOUNT
FROM CUSTOMERS
LEFT JOIN
	ORDERS
ON
	CUSTOMERS.CUSTOMER_ID = ORDERS.CUSTOMER_ID;

-- Right Join: Retrieve all orders and their customers, including orders with no customers
SELECT
	CUSTOMERS.CUSTOMER_NAME,
    CUSTOMERS.EMAIL_ADDRESS,
    ORDERS.ORDER_STATUS,
    ORDERS.TOTAL_AMOUNT
FROM CUSTOMERS
RIGHT JOIN
	ORDERS
ON
	CUSTOMERS.CUSTOMER_ID = ORDERS.CUSTOMER_ID;

-- Full Outer Join
-- Retrieve a list of all customers and their orders, 
-- including customers without orders and orders without customers. 
-- (Note: MySQL does not support FULL OUTER JOIN directly, so we use a UNION of LEFT JOIN and RIGHT JOIN.)
-- Full Outer Join: Retrieve all customers and orders, including customers with no orders and orders with no customers
SELECT
	CUSTOMERS.CUSTOMER_NAME,
    CUSTOMERS.EMAIL_ADDRESS,
    ORDERS.ORDER_STATUS,
    ORDERS.TOTAL_AMOUNT
FROM CUSTOMERS
LEFT JOIN
	ORDERS
ON
	CUSTOMERS.CUSTOMER_ID = ORDERS.CUSTOMER_ID

UNION

SELECT
	CUSTOMERS.CUSTOMER_NAME,
    CUSTOMERS.EMAIL_ADDRESS,
    ORDERS.ORDER_STATUS,
    ORDERS.TOTAL_AMOUNT
FROM CUSTOMERS
RIGHT JOIN
	ORDERS
ON
	CUSTOMERS.CUSTOMER_ID = ORDERS.CUSTOMER_ID;
-- Cross Join
-- Cross join, also known as Cartesian join, returns the Cartesian product of the two tables, meaning it pairs every row from the first table with every row from the second table. 
-- While this may seem impractical and can result in very large result sets, it has specific uses in certain scenarios.
-- Retrieve a Cartesian product of all customers and orders. This will pair each customer with every order.
-- In our example Cross Join: Retrieve Cartesian product of customers and orders
SELECT
	CUSTOMERS.CUSTOMER_NAME,
    CUSTOMERS.EMAIL_ADDRESS,
    ORDERS.ORDER_STATUS,
    ORDERS.TOTAL_AMOUNT
FROM CUSTOMERS CROSS JOIN ORDERS;

-- SELF JOIN ---

-- Create a Table
CREATE TABLE Employee (
    EmployeeID INT PRIMARY KEY,
    Emp_Name VARCHAR(55),
    ManagerID INT
);

-- Insert Sample Data
INSERT INTO Employee
(EmployeeID, Emp_Name, ManagerID)
VALUES
(1, 'Mike', 3),
(2, 'David', 3),
(3, 'Roger', NULL),
(4, 'Marry',2),
(5, 'Joseph',2),
(7, 'Ben',2);

-- Check the data
SELECT 
    *
FROM
    Employee;

-- Inner Join
SELECT 
	e1.Emp_Name AS employee_name,
    e2.Emp_Name AS manager_name
FROM
	EMPLOYEE e1
    INNER JOIN
    EMPLOYEE e2
ON
	e1.managerID = e2.employeeID;
    
-- Outer Join
SELECT
	e1.Emp_Name employee_name,
FROM
	EMPLOYEE e1
    LEFT JOIN
    EMPLOYEE e2
ON
	e1.managerID = e2.employeeID;
    
-- Outer join column name change if null
SELECT
	e1.Emp_Name employee_name,
    ifnull(e2.Emp_Name, 'top manager') AS manager_name
FROM
	EMPLOYEE e1
		LEFT JOIN
    EMPLOYEE e2
ON
	e1.managerID = e2.employeeID;

-- Clean up (optional)


-- Sub-query
-- Subquery in the WHERE Clause
-- Find customers who have placed at least one order.
-- The IN operator is used to filter the results of a query based on a list of values. 
-- In this case, the subquery (SELECT CUSTOMER_ID FROM ORDERS) generates a list of CUSTOMER_IDs that have placed orders. 
-- The outer query then retrieves customer details for those CUSTOMER_IDs that appear in this list.

SELECT 
	customer_name,
    phone,
    email_address
FROM customers
WHERE
	customer_id IN (SELECT customer_id FROM ORDERS);