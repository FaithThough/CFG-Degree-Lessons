USE bank;
-- Create a SF that accepts customer account's balance as a parameter 
-- and assesses whether they are eligible for credit

SELECT * FROM accounts;

DELIMITER //

CREATE FUNCTION credit_eligible(
    balance INT
)
RETURNS VARCHAR(20)
DETERMINISTIC
BEGIN
    DECLARE customer_status VARCHAR(20);
    
    IF balance >= 100 THEN
        SET customer_status = 'yes';
    ELSEIF (balance >= 50 AND balance < 100) THEN
        SET customer_status = 'maybe';
    ELSE 
        SET customer_status = 'no';
    END IF;
    
    RETURN(customer_status);
END //

DELIMITER ;

DELIMITER ;

SELECT
	account_number,
    account_holder_name,
    account_holder_surname,
    balance,
credit_eligible(balance) as 'eligible'
FROM
	accounts;


