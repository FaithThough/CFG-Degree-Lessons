CREATE DATABASE property_reviews;
USE property_reviews;

-- Properties Table
CREATE TABLE properties (
    property_id INT PRIMARY KEY,
    property_name VARCHAR(255),
    city VARCHAR(100),
    price VARCHAR(10),
    company_name VARCHAR(255)
);
-- Reviews Table
CREATE TABLE reviews (
    review_id INT PRIMARY KEY,
    property_id INT,
    review_text TEXT,
    score INT,
    FOREIGN KEY (property_id) REFERENCES properties(property_id)
);
-- Sample Data for Properties Table:
INSERT INTO properties (property_id, property_name, city, price, company_name)
VALUES
  (1, 'Cozy Apartment', 'CityA', "$100", 'Property Management A'),
  (2, 'Spacious Condo', 'CityB', "$150", 'Property Management B'),
  (3, 'Luxury Villa', 'CityC', "$300", 'Property Management C'),
  (4, 'Downtown Loft', 'CityA', "$120", 'Property Management A'),
  (5, 'Seaside Cottage', 'CityB', "$80", 'Property Management B');

SELECT * FROM properties;

-- Sample Data for Reviews Table with Words 'dirty,' 'cleaning,' or 'clean'
INSERT INTO reviews (review_id, property_id, review_text, score)
VALUES
  (101, 1, 'Perfect place for families. Spacious rooms and kid-friendly amenities.', 5),
  (102, 2, 'Family vacation was a delight. Beautiful view from the condo.', 4),
  (103, 3, 'Great for families. Kids loved the pool in the villa.', 5),
  (104, 4, 'Ideal for a family getaway. Downtown location added convenience.', 3),
  (105, 5, 'Family enjoyed the seaside cottage. Clean and comfortable.', 4),
  (106, 1, 'The apartment was dirty. Needs cleaning urgently!', 2),
  (107, 2, 'Clean and tidy. No issues at all.', 5),
  (108, 3, 'Just average.', 3),
  (109, 4, 'Nice place for stay. Kid friendly', 4),
  (110, 5, 'Perfect location.', 2);
  
SELECT * FROM reviews;
  
  -- Clean the data and remove the currency sign before the price. Ensure to preserve the values without the currency sign in a new column.
SELECT REPLACE(price, '$', '') AS stripped_price FROM properties;
ALTER TABLE properties ADD COLUMN stripped_price VARCHAR(10);
UPDATE properties
SET stripped_price = REPLACE(price, '$', '');

-- Find how much the top 3 properties from the company list are earning
SELECT stripped_price
FROM properties
ORDER BY stripped_price ASC
LIMIT 3;

-- Write a query to retrieve properties suitable for families with amenities like spacious rooms and a kid-friendly environment
SELECT *
FROM reviews
WHERE review_text LIKE '%spacious rooms%' OR review_text LIKE '%kids%' OR review_text LIKE '%family%' OR review_text LIKE '%families';

-- Create a stored procedure to fetch the details of the most expensive property in each city
DELIMITER //

CREATE PROCEDURE most_expensive_property_in_each_city()
BEGIN
	SELECT p1.*
    FROM properties p1
    INNER JOIN(
    SELECT city, MAX(price) AS max_price
    FROM properties
    GROUP BY city
    ) p2
    ON p1.city = p2.city AND p1.price = p2.max_price;
END //

DELIMITER ;

CALL most_expensive_property_in_each_city;

-- Lowest score
SELECT MIN(score) FROM reviews;

-- Lowest average review score
DELIMITER //
CREATE FUNCTION average_review_score (property_id INT)
RETURNS INT
READS SQL DATA
BEGIN
	DECLARE average_score INT;
	SELECT AVG(score)
    INTO average_score
    FROM reviews
    WHERE property_id = property_id;
    
    RETURN average_score;
END //

DELIMITER ;

SELECT average_review_score(1);
SELECT average_review_score(2);
SELECT average_review_score(3);
SELECT average_review_score(4);
SELECT average_review_score(5);

-- Write a query to find the property with the lowest average review score.
SELECT property_id, AVG(score) AS avg_score
FROM reviews
GROUP BY property_id
ORDER BY avg_score ASC
LIMIT 1;




