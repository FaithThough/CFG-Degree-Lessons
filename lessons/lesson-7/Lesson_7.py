# Comparison operators
print (7 == 7)
print("Faith" == "Faith")
print (19 != 4)
print (19 < 4)
print (19 > 4)
print (19 <= 4)
print (19 >= 4)

# Logical operators

# If elif, else statement
# name = input("Enter your name ")
# stored_name = "Faith"
# alternate_name = "admin"
# if name == stored_name:
#     print("Welcome to your dashboard")
# elif name == alternate_name:
#     print("Hello admin")
# else:
#     print("Access denied")

# Practice
# burger_price = float(input("Enter the price of the burger"))
# if burger_price <= 10.00:
#     print("Burger is within budget 🍔")
# else:
#     print("Burger is not within budget 🚫")

# Logical operators
# name = input("Enter your name ")
# password = input("Enter your password ")
# stored_name = "Faith"
# alternate_name = "admin"
# stored_password = "password"
# if name == stored_name and password == stored_password:
#     print("Welcome to your dashboard")
# elif name == alternate_name and password == stored_password:
#     print("Hello admin")
# else:
#     print("Access denied")

# # Own example
# temperature = int(input("Enter the current temperature: "))
# if temperature > 65 and temperature < 75:
#     print("System maintained")
# elif temperature < 65:
#     print("Heating activated")
# else:
#     print("Air conditioning activated")

# # Practice
# temperature = int(input("Enter the oven temperature: "))
# if temperature > 200:
#     print("The oven is too hot")
# elif temperature < 150:
#     print("The oven is too cold")
# elif temperature == 180:
#     print("The oven is at the perfect temperature")
# else:
#     print("The temperature is close enough")

# and or
print(7 == 7 and 14 == 14) #true
print(7 == 7 and 14 == 13) #false
print(7 == 7 or 14 == 3) #true

# My example
# overdue_books = input("Do you have any overdue books? y/n ")
# valid_membership = input("Do you have a valid membership? y/n ")
# special_guest_pass = input("Do you have a special guest pass? y/n ")
# if overdue_books == "n" and valid_membership == "y":
#     print("You can borrow a book")
# elif valid_membership  == "y" or special_guest_pass  == "y":
#     print("You can borrow an e-book")
# else:
#     print("You may not borrow any books or e-books")

# if not
# logged_in = input("Are you logged in? (yes/no) ").lower()
# if not logged_in == "yes":
#     print("Please log in to continue")
# else:
#     print("Welcome back!")

# Debugging
# month = input("What month is it? ")
#
# if month == "April" or month == "June" or month == "September" or month == "November":    print("There are 30 days in this month")
# elif month == "February":
#     leap_year = input("Is it a leap year?")
#     if leap_year == "yes":
#         print("There are 29 days in this month")
#     else:
#         print("There are 28 days in this month")
# else:
#     print("There are 31 days in this month")

#random
import random
random_integer = random.randint(1,6)
print(random_integer)

# Palindrome
# Checking whether strings are palindrome or not
def is_palindrome(s):
    lower = s.lower()
    return lower == s[::-1] #reversing everything and then comparing

string = "hannah"
if is_palindrome(string):
    print("Yes, it is a palindrome")
else:
    print("No it is not a palindrome")

# alternative
word = input("Enter a word ")
new_word = ""
for letter in word:
    new_word= letter + new_word

if word == new_word:
    print("Yes, it is a palindrome")
else:
    print("No it is not a palindrome")