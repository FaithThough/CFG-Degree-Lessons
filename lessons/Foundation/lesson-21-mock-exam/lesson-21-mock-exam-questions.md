# MOCK EXAM

# Theory questions [31 marks]

### 1.1 Name the stages of the Software Development Lifecycle

- Requirements
- Analysis
- Design
- Coding
- Testing
- Operations

### 1.2 What exception is thrown when you divide a number by 0? (1 mark)

Zero division error

### 1.3 What is the git command that moves code from the local repository to the remote repository? (1 mark)

git push

### 1.4 What does NULL represent in a database? (1 mark)

no value

### 1.5 Name 2 responsibilities of the Scrum Master. (2 marks)

- Facilitating scrum ceremonies
- Removing blockers and impediments
- Ensuring the team follow the scrum framework

### 1.6 Name 2 debugging methods, and when you would use them. (4 marks)

<table>
    <tbody>
        <tr>
            <td>
                Method
            </td>
            <td>
                Description
            </td>
            <td>
                Use case
            </td>
        </tr>
        <tr>
            <td>
                Print debugging
            </td>
            <td>
                Inserting print statements into the code to display the values of variables and the state of the program at certain points in its execution. This information can then be used to identify the source of errors and fix them.
            </td>
            <td>
                <strong>Simple debugging tasks: </strong>when you need to quickly check the value of variables or the flow of execution in small or simple programs<br>
                <br>
                <strong>Understanding program flow: </strong>when you need to understand how your programme is executing especially in loops, conditionals or recursive functions
            </td>
        </tr>
        <tr>
            <td>
                Backtracking
            </td>
            <td>
                Analysing the programs execution history to find the cause of the bug. Instead of just looking at the current state of the program, you can move backward through the execution to see the sequence of events and states that led to the error.
            </td>
            <td>
                <strong>Complex bugs:</strong> dealing with complex or intermittent bugs that are hard to reproduce or understand from the current state<br>
                <br>
                <strong>Understanding state changes:</strong> when you need to understand how the state of the program has changed over time leading up to the error<br>
                <br>
                <strong>Historic state analysis: </strong>when you need to analyse the historic values of variables and the control flow leading to a specific point
            </td>
        </tr>
    </tbody>
</table>

1.7 Looking at the following code, describe a case where this function would throw an error when called. Describe this case and talk about what exception handling you’ll need. (5 marks)

```python
def can_pay(price, cash_given):
    if cash_given >= price:
        return True
    else:
        return False
```

- Should we assign a variable for price and a user input for cash given:

```python
price = 10
cash_given = input('How much cash do you have ?')
```

- This function would throw the following error:

![Untitled](MOCK%20EXAM%20b0173a00eb0b416b96511c0e523429a7/Untitled.png)

- This is because when we ask the user for an input, whatever is entered is considered a string:

```python
cash_given = input('How much cash do you have? ')
print(type(cash_given))
```

![Untitled](MOCK%20EXAM%20b0173a00eb0b416b96511c0e523429a7/Untitled%201.png)

- You cannot use a comparison operator on a string
- In order to error handle, we need to turn the input into a integer:

```python
cash_given = int(input('How much cash do you have? '))
print(type(cash_given))
```

![Untitled](MOCK%20EXAM%20b0173a00eb0b416b96511c0e523429a7/Untitled%202.png)

### 1.8 What is git branching? Explain how it is used in Git. (6 marks)

- If we think of a tree with the main trunk representing the main branch
- From this trunk, branches can grow
- If you were working on a new feature you may create a new branch, not wanting to change/affect the main branch
- A branch is a snapshot of a project at a specific point in time so you can work on it independently
- Once the feature is completed and tested it can be merged into the main branch

### 1.9 Design an in-house restaurant ordering system. You do not need to write code, but describe a high-level approach: (10 marks)

### a. Write a list of key requirements.

- Food dictionary that contains food items and prices
- Drink dictionary that contains drink items and prices
- Support for special instructions or customizations (e.g., dietary restrictions, modifications to menu items)
- Input that allows the user to ‘order’ their food and drink
- Output that tells the user how much their meal costs
- Ensuring that the user has enough to pay for their meal
- Ensuring that the items are in stock and available to order
- Ability to track orders and their status (e.g., placed, preparing, ready for pickup/delivery)
- Allowing the user to leave a tip
- Reporting and analytics (e.g., popular items, sales data)

### b. What are your main considerations and problems?

- Ensuring that the user only picks items from the menu and error handling if not
- Ensuring that the user is told if an item is out of stock and given the option to order something else if so
- Ensuring that the user can order multiple items
- Taking the users input for the cash they have as a string and turning it into an integer
- Adding and removing items from the menu on an ad hoc basis e.g. if something was out of stock or there was a special

### c. What components or tools would you potentially use?

- Dictionaries for the food and drink items
- Database (e.g., MySQL) for storing menu items, orders, and user data
- Prompt input for the user to order
- Function to add up item prices and work out whether the user has enough money
- If else statement to determine whether the user can afford to dine
- Payment gateway integration (e.g., Stripe, PayPal) if accepting payments


# Section One: Multiple Choice Questions [10 marks]

1. **What is the output of the Python equation “5 // 2”?**
    
    A. 2
    
2. **What would be the first line and last line output of the following Python code?**
    
    D. First line:
         Last line: +++++++++
    
3. **Which of these is not a necessary feature of a function definition?**
    
    A. return statement 
    
4. **Which statement is true about the functionality of Python’s `pass` statement?**
    
    D. It doesn’t add any new functionality
    
5. **Which of the following creates a list with the first 5 natural squared numbers?**
    
    B. `list = [i**2 for i in range(1,6)]`
    
6. **Which SQL statement is used to remove a table?**
    
    C. Drop
    
7. **The HR department needs to find employees who have joined the company within the last three months. Which SQL query will help achieve this?**
    
    C. `SELECT * FROM employees WHERE hire_date >= SYSDATE - INTERVAL '3' MONTH;`
    
8. **Which SQL statement adds a new column to an existing table?**
    
    A. `ALTER TABLE table_name ADD column_namedata_type;`
    
9. **The marketing team wants to find the total sales for each product category. What SQL query would provide this information?**
    
    A. `SELECT category,SUM(sales) FROM products GROUP BY category;`
    
10. **A company wants to know the total number of products with an available status in the "inventory" table. What SQL query can be used to obtain this information?**
    
    B. `SELECT COUNT(*) FROM inventory WHERE status='available';`
    

# Section Two: Code/Query Evaluation [15 marks]

Consider a scenario where a healthcare authority of a 1500-bed hospital aims to retrieve the total number of patients admitted to each department within a specified timeframe.

The existing query is as follows:

```sql
SELECT
	department_id
	count(*) AS total_admissions
FROM
	admissions
WHERE
	admission_date BETWEEN 'start_date' AND 'end_date'
GROUP BY
	department_name;
LIMIT 1
```

Evaluate the given code. You should:

1. Identify and correct any errors in the code - include any corrected code snippets alongside your written answer.
- This block:

```sql
SELECT
	department_id
	count(*) AS total_admissions
```

- Requires a comma after department_id so the alias total_admissions will be assigned to the count(*) column in the output:

```sql
SELECT
	department_id, 
	count(*) AS total_admissions
```

- This line:

```sql
WHERE
	admission_date BETWEEN 'start_date' AND 'end_date'
```

- `start_date` and `end_date` need to be initialised variables:

```sql
WHERE
	admission_date BETWEEN '2023-01-01' AND '2023-12-31'
```

- This line:

```sql
LIMIT 1
```

- Limits the results to only 1 row which wouldn’t allow us to retrieve the total number of patients admitted to each department within a specified timeframe.
- It should be removed
- This line:

```sql
GROUP BY
	department_name;
```

- Should consider grouping by department_id since the select statement includes department_id:

```sql
GROUP BY
	department_id;
```

- In summary, the improved code would look like this:

```sql
SELECT
    department_id, 
    count(*) AS total_admissions
FROM
    admissions
WHERE
    admission_date BETWEEN '2023-01-01' AND '2023-03-31'
GROUP BY
    department_id;
```

1. Provide three specific suggestions for improving or optimizing the code.
- **Use parameterized queries** instead of hard coding the date values in the where clause:

```sql
CREATE PROCEDURE GetTotalAdmissionsByDepartment
    @StartDate DATE,
    @EndDate DATE
AS
BEGIN
    SELECT
        department_id,
        COUNT(*) AS total_admissions
    FROM
        admissions
    WHERE
        admission_date BETWEEN @StartDate AND @EndDate
    GROUP BY
        department_id;
END
```

- This will allow us to:
    - Pass different date ranges dynamically
    - Improve query performance by enabling reuse
- **Create an index**
- If the admissions table is large and queries involving the admission_date colum are frequent we should consider creating an index on the admission_date colum

```sql
CREATE INDEX idx_admissions_admission_date
ON admissions (admission_date);
```

- This will improve query performance by allowing the database to quickly locate relevant rows
- Utilise aliases

```sql
SELECT
    d.department_id AS dept_id,
    COUNT(*) AS total_admissions
FROM
    admissions a
    JOIN departments d ON a.department_id = d.department_id
WHERE
    a.admission_date BETWEEN '2023-01-01' AND '2023-03-31'
GROUP BY
    d.department_id;
```

- This makes the code more readable and easier to distinguish the columns from different tables

# Section Three: Coding Challenge [25 marks]

- See lesson-21-mock-coding-challenge.py