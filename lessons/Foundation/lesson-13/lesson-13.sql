-- SELECT DATABASE();
-- SHOW DATABASES;

CREATE DATABASE Bakery;
USE Bakery;
SELECT DATABASE();
CREATE TABLE Sweet(
	id INT NOT NULL,
    item_name VARCHAR(50) NOT NULL,
    price FLOAT(2)
);

SHOW TABLES;

DESC sweet;

SELECT * FROM sweet WHERE price < 1.5;

INSERT INTO sweet(id,item_name,price)
VALUES
(1,'Doughnut',0.50),
(2,'Blueberry Muffin',1.50),
(3,'Croissant',1.00),
(4,'Lemon Tart',2.00),
(5,'Banana Bread',1.75),
(6, 'Apple Pie', 1.25);

CREATE TABLE savoury(
    id INT NOT NULL,
    item_name VARCHAR(50) NOT NULL,
    price FLOAT(2),
    main_ingredient VARCHAR(50) NOT NULL
);

SELECT * FROM savoury;

INSERT INTO savoury(id,item_name,price,main_ingredient)
VALUES
(1,'Cheese Scone',2.50,'cheese'),
(2,'Spinach and Feta Pastry',1.50,'spinach'),
(3,'Ham and Cheese Croissant',3.75,'ham'),
(4,'Bacon and Egg Muffin',4.00,'bacon'),
(5,'Garlic Bread',2.00, 'garlic'),
(6, 'Chicken Pie', 3.20, 'chicken'),
(7, 'Sausage Roll', 2.50, 'sausage');

SELECT 
savoury.item_name,
savoury.price
FROM savoury;
