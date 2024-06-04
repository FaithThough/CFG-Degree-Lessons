CREATE DATABASE customers;


USE customers;

CREATE TABLE customer_information(
C_ID INTEGER PRIMARY KEY,
first_name VARCHAR (50),
email VARCHAR (30)
);

INSERT INTO customer_information
VALUES (1, 'Faith', 'Faith@gmail.com');

SELECT * from customer_information;