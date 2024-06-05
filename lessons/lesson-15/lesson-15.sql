USE bakery;
SELECT * FROM SWEET;
SELECT * FROM SAVOURY
WHERE PRICE > 2;

SELECT * FROM SAVOURY
WHERE ITEM_NAME = 'cheese scone';

SELECT * FROM SAVOURY
WHERE ID > 3 AND item_name = 'chicken pie';

SELECT * FROM SWEET
WHERE ID < 2 OR item_name LIKE '%e%';

-- Find all savoury items that have a bacon or sausage filling
SELECT item_name FROM SAVOURY
WHERE main_ingredient = 'bacon' or main_ingredient = 'sausage';

-- Find all sweet items that cost £1 or less
SELECT item_name FROM SWEET
WHERE price <= 1;

-- Find all sweet items and their price, except for apple pie
SELECT item_name, price
FROM SWEET
WHERE item_name != 'apple pie';

-- Find all sweet names that start with the letter 'c'
SELECT item_name
FROM SWEET WHERE item_name LIKE 'c%';

-- Find all savoury items that cost more than £1 but less than £3
SELECT item_name, price
FROM SAVOURY WHERE price BETWEEN 1 AND 3;

-- Use various set functions to see how they work in practice
SELECT COUNT(item_name) AS 'number of items'
FROM SWEET;

SELECT ROUND(AVG(price), 2) AS 'average price'
FROM SAVOURY;

