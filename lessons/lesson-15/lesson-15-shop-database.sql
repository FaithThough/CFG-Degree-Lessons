CREATE DATABASE shop;
use shop;

CREATE TABLE SALES1 (
    Store VARCHAR(20) NOT NULL,
    Week VARCHAR(20) NOT NULL,
    Day VARCHAR(20) NOT NULL,
    SalesPerson VARCHAR(20) NOT NULL,
    SalesAmount DECIMAL(6 , 2 ) NOT NULL,
    Month VARCHAR(20) NULL
); 

INSERT INTO  SALES1
(Store, Week, Day, SalesPerson, SalesAmount, Month) 
VALUES 
('London', '2', 'Monday', 'Frank', CAST(56.25 AS Decimal(6, 2)), 'May'),
('London', '5', 'Tuesday', 'Frank', CAST(74.32 AS Decimal(6, 2)), 'Sep'),
('London', '5', 'Monday', 'Bill', CAST(98.42 AS Decimal(6, 2)), 'Sep'),
('London', '5', 'Saturday', 'Bill', CAST(73.90 AS Decimal(6, 2)), 'Dec'),
('London', '1', 'Tuesday', 'Josie', CAST(44.27 AS Decimal(6, 2)), 'Sep'),
('Dusseldorf', '4', 'Monday', 'Manfred', CAST(77.00 AS Decimal(6, 2)), 'Jul'),
('Dusseldorf', '3', 'Tuesday', 'Inga', CAST(9.99 AS Decimal(6, 2)), 'Jun'),
('Dusseldorf', '4', 'Wednesday', 'Manfred', CAST(86.81 AS Decimal(6, 2)), 'Jul'),
('London', '6', 'Friday', 'Josie', CAST(74.02 AS Decimal(6, 2)), 'Oct'),
('Dusseldorf', '1', 'Saturday', 'Manfred', CAST(43.11 AS Decimal(6, 2)), 'Apr');

-- Find how many sales took place each week (in not particular order)
SELECT WEEK, COUNT(*)
FROM SALES1
GROUP BY WEEK;

-- Select all stores from the SALES1 table and order the results in descending order by the store name.
SELECT Store FROM SALES1
ORDER BY STORE DESC;

-- Select the store and the count of sales records for each store,
-- grouping the results by the store and filtering to include only the London store.
SELECT STORE, COUNT(*)
FROM SALES1
GROUP BY Store
HAVING Store = 'London';

-- Find all sales records (and all columns) that took place in the London store, not 
-- in December which were conducted by Bill or Frank for and amount higher than £50
SELECT *
FROM SALES1
WHERE store = 'London' 
  AND month != 'Dec'
  AND SalesAmount > 50
  AND (SalesPerson = 'Bill' OR SalesPerson = 'Frank');
  