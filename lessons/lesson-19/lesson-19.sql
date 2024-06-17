use ecomerce;
SELECT * FROM customers;
SELECT * FROM orders;

-- Inner join
SELECT orders.order_id, customers.customer_id
FROM ORDERS
INNER JOIN customers ON orders.customer_id = customers.customer_id;

-- Left join
SELECT orders.order_id, customers.customer_id
FROM orders
LEFT JOIN customers ON orders.customer_id = customers.customer_id
ORDER BY order_ID ASC;

-- Right join
SELECT orders.order_id, customers.customer_id
FROM orders
RIGHT JOIN customers ON orders.customer_id = customers.customer_id;