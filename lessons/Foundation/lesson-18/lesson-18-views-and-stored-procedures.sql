USE ecomerce;

SELECT * FROM ORDERS;

-- Sub-query
-- Subquery in the WHERE Clause
-- Query to find customers who have placed at least one order.
-- The IN operator is used to filter the results of a query based on a list of values. 
-- In this case, the subquery (SELECT CUSTOMER_ID FROM ORDERS) generates a list of CUSTOMER_IDs that have placed orders. 
-- The outer query then retrieves customer details for those CUSTOMER_IDs that appear in this list.
SELECT 
	CUSTOMER_NAME,
    PHONE,
    EMAIL_ADDRESS
FROM CUSTOMERS
WHERE 
	CUSTOMER_ID IN (SELECT CUSTOMER_ID FROM ORDERS);

-- VIEWS
-- A view is a virtual table based on the result-set of an SQL statement

-- Display all orders amount > 20 
CREATE OR REPLACE VIEW vw_orders_greater_than_20
AS 
	SELECT ORDER_ID, TOTAL_AMOUNT 
    FROM ORDERS
    WHERE total_amount > 20;
    
SELECT * FROM vw_orders_greater_than_20;

-- Display all orders who's status is delivered
-- Now, I want only order_id,customer_id and status to be visible, other fields I don't want to show
CREATE OR REPLACE VIEW vw_delivered
AS 
	SELECT order_id,customer_id, order_status
    FROM ORDERS
    WHERE ORDER_STATUS = 'delivered'
WITH CHECK OPTION;

SELECT * FROM vw_delivered;

-- Lets add a new order with a status Dispatched, it shouldn't be visible in the view
-- Also check it will be in the list of orders
START TRANSACTION;
INSERT INTO ORDERS(ORDER_ID, ORDER_STATUS, TOTAL_AMOUNT, QUANTITY, CUSTOMER_ID)
VALUES
(6, 'Dispatched', 48, 4, 3);

INSERT INTO ORDERS(ORDER_ID, ORDER_STATUS, TOTAL_AMOUNT, QUANTITY, CUSTOMER_ID)
VALUES
(7, 'Dispatched', 32, 3, 2);

INSERT INTO ORDERS(ORDER_ID, ORDER_STATUS, TOTAL_AMOUNT, QUANTITY, CUSTOMER_ID)
VALUES
(8, 'Processed', 39, 6, 4);

SELECT * FROM vw_delivered;
SELECT * FROM ORDERS WHERE ORDER_ID = 6;
SELECT * FROM ORDERS WHERE ORDER_ID = 7;
COMMIT;

-- Let's modify the view to add WITH CHECK OPTION and see how it behaves. 
-- Display all orders who's status is delivered
SELECT * FROM vw_delivered;

-- The WITH CHECK OPTION clause indicates that any updated or inserted row to the view must be checked against the view definition, 
-- and rejected if it does not conform.
-- This will fail because ORDER_STATUS is not 'delivered'
INSERT INTO vw_delivered (order_id, customer_id, order_status)
VALUES (9, 4, 'processed');

-- Try inserting an order with status Dispatched and Delivered#
-- Delivered will work as its as per the condition in the view
-- This will succeed because ORDER_STATUS is 'delivered'
INSERT INTO vw_delivered (order_id, customer_id, order_status)
VALUES (9, 4, 'delivered');

-- DROP VIEW using 
-- DROP VIEW (VIEW_NAME)
-- DROP VIEW vw_orders_greater_than_20;

-- ---------------------------

-- STORED PROCEDURE
-- Create a basic SP to display Greetings to User
DELIMITER //

CREATE PROCEDURE user_greeting(message VARCHAR(30),first_name VARCHAR(20))
BEGIN
    DECLARE user_greeting_message VARCHAR(50);
    SET user_greeting_message = CONCAT(message, ' ', first_name);
    SELECT user_greeting_message AS 'Greeting message'; 
END //

DELIMETER;

-- Call Greetings SP
CALL user_greeting ('Hello', 'Faith');
CALL user_greeting ('Hi', 'Marcus');

-- Lets create an auto procedure that allows us to insert values in a table in one line code
SELECT * FROM ORDERS;

DELIMITER //
CREATE PROCEDURE sp_insert_orders(
	IN o_status VARCHAR(30),
    IN t_amount INT,
    IN o_quantity INT,
    IN c_id INT
)
BEGIN
	INSERT INTO ORDERS(ORDER_STATUS, TOTAL_AMOUNT, QUANTITY, CUSTOMER_ID)
    VALUES(o_status,t_amount,o_quantity,c_id);
END //

DELIMITER ;

-- Call insert SP
CALL sp_insert_orders('Dispatched', 50, 3, 1);
SELECT * FROM ORDERS; 

-- Drop SP
-- DROP procedure [SP_NAME];
-- DROP PROCEDURE user_greeting;

-- A Store procedure to fetch the order details by order ID
