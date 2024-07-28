CREATE TABLE products(
	product_id INT PRIMARY KEY,
    product_name VARCHAR(100),
    stock INT
);

CREATE TABLE orders(
order_id INT PRIMARY KEY AUTO_INCREMENT,
product_id INT,
quantity INT,
order_date DATETIME,
FOREIGN KEY (product_id) REFERENCES products(product_id)
);

INSERT INTO products(product_id, product_name, stock)
VALUES
(1, 'Laptop', 50),
(2, 'Smartphone', 120),
(3, 'Tablet', 80),
(4, 'Headphones', 150),
(5, 'Smartwatch', 70),
(6, 'Monitor', 40),
(7, 'Keyboard', 200),
(8, 'Mouse', 180),
(9, 'Printer', 30),
(10, 'Router', 90);

SELECT * FROM products;

INSERT INTO orders(product_id, quantity, order_date)
VALUES
(1, 2, '2024-06-01 10:15:00'),
(2, 1, '2024-06-02 11:20:00'),
(3, 5, '2024-06-03 14:30:00'),
(4, 3, '2024-06-04 09:45:00'),
(5, 2, '2024-06-05 16:50:00'),
(6, 1, '2024-06-06 12:05:00'),
(7, 4, '2024-06-07 13:25:00'),
(8, 3, '2024-06-08 17:40:00'),
(9, 2, '2024-06-09 08:55:00'),
(10, 1, '2024-06-10 15:35:00');

SELECT * from orders;

DELIMITER $$

CREATE PROCEDURE insert_order(
IN p_product_id INT,
IN p_quantity INT
)

BEGIN 
	DECLARE v_stock INT;
    
    -- check current stock
    SELECT stock INTO v_stock 
    FROM products
    WHERE product_id = p_product_id;
    
    -- check if sufficient stock is availible 
    IF v_stock >= p_quantity THEN 
		-- insert order
        INSERT INTO orders(product_ID, quantity, order_date)
        VALUES (p_product_id, p_quantity, NOW());
        
        -- update stock
        UPDATE products
        SET stock = stock - p_quantity
        WHERE product_id = p_product_id;
        
        SELECT 'Order inserted successfully' AS message;
	ELSE
		SELECT 'Insufficient stock' AS message;
        
	END IF;
END$$
DELIMITER ;

-- SQL injection
SELECT * FROM users WHERE username = 'username' 
AND password = 'password'

        




