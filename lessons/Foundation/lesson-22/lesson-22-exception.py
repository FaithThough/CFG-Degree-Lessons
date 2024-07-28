# Take input from user and divide the values

# # Type error
# a = (input('Please enter a number to divide: '))
# b = (input('Please enter a number to divide by: '))
# answer = a/b
# print(answer)

# a = int(input('Please enter a number to divide: '))
# b = int(input('Please enter a number to divide by: '))
# answer = a/b
# print(answer)

# Using a try block
a = float(input('Please enter a number to divide: '))
b = float(input('Please enter a number to divide by: '))
try:
    answer = a/b
    print(f"{answer:.2f}")  # Format the answer to 2 decimal places

except ZeroDivisionError:
    print("You can't divide by zero, please try again")
except ValueError:
    print("Incorrect value, try putting a whole number")

else:
    print("Your division is successful")
# Free up your resource - closing a file, closing a DB connection
finally:
    print("I am the finally block")