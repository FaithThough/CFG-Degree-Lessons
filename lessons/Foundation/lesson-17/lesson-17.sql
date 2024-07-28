USE bakery;
SELECT * FROM sweet;

-- Deleting data from a table
DELETE FROM sweet 
WHERE ID = '6';

-- Deleting something else
-- Alternatively: BEGIN;
START TRANSACTION;

DELETE FROM sweet
WHERE ID = '5';

-- Undo changes
ROLLBACK;

-- Commit changes
-- COMMIT;

-- Functions
-- String functions
SELECT CONCAT('Hello', ' ', 'world') AS greeting;
SELECT LENGTH('HELLO') AS string_length;
-- Numeric functions
SELECT CEIL (10.1) AS ceiling_value;
-- Returns the smallest integer value greater than or equal to a number
SELECT ROUND(10.342, 2) AS rounded_number;
-- Date functions
-- Wrap date in single quotes
SELECT NOW();
SELECT CURDATE() AS date;
SELECT CURTIME() AS time;
SELECT YEAR(NOW()) AS current_year;
SELECT MONTH(NOW()) AS current_month;
SELECT DATE_FORMAT('2021-09-20 11:22:00', '%W %M %Y') AS anniversary;
