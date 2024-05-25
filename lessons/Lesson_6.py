# User input
# first_name = input("What is your first name? ")
# last_name = input("What is your last name? ")
# age = int(input("What is your age? "))
# # input method always returns a string
# # print("Hello", first_name, last_name)
# print(f"Hello {first_name} {last_name} you are {age} years old")
# age_in_3_years = age + 3
# print(f"After 3 years you will be {age_in_3_years}")

# Modules - date time
import datetime
currentDate = datetime.datetime.now()
print(currentDate)

# Fetching date with format
myDate = datetime.date(2024,0o5,21)
print(myDate.strftime("%d/%b/%Y"))
# d returns day of month
# b return the first three characters of the month
# y returns the year in a 4 digit format

# For loop
# print("1") #print 10 times

for number in range(10):
    print(number + 1)
print("End of loop")

# printing odd numbers
for number in range(1,11,2):
    print(number)
print("End of loop")

# printing even numbers
for number in range(2,11,2):
    print(number)
print("End of loop")

# Use of while loop
# A store capacity of 10 people, after that we will print a message to ask people to wait in the queue

store_capacity = 10

while store_capacity > 0:
    print(f"Please come in, spaces availible: {store_capacity}")
    store_capacity = store_capacity - 1

print("\nPlease wait for someone to exit the store, capacity has been reached")
# Upon reaching 1 it comes out of the loop

# Functions
# Define the function
# def hello():
#     print("Hello everyone ")
#
# # Calling the function
# hello()

# Function that takes an argument
# def hello(name):
#     print(f"Hello {name}")
#
# # Calling the function
# hello("Faith")
# hello("Marcus")
# hello("Miley")
# hello("AJ")

# # Passing in multiple values
# def hello(first_name, last_name):
#     print(f"Hello {first_name} {last_name}")
#
# # Calling the function
# hello("Faith", "Phillips")
# hello("Marcus", "Ojerinde-Ardalla")
# hello("Miley", "Large")
# hello("AJ", "Large")

# Order of arguments
def hello(first_name, job = 'developer'):
    print(f"Hello {first_name} you work as a {job}")

# Calling the function
hello("Faith", "Software Engineer") # arguments in correct position and order
hello(job = "Software Engineer", first_name= "Faith") # keyword arguments to specify the parameter
hello("Luna") # Calling the funciton with a default argument for job

# Unknown number of arguments
def print_number(*args):
    print(args)

print_number(1,2,3,4,5,6,7,8,9)
print_number(1,2,3)

# Print with **key word arguments
def print_employees(**kwargs):
    print(kwargs)

print_employees(name="Faith", age = 27)
print_employees(name = "Marcus", job= "Data Engingeer")

# Return statement
def sum(x,y):
    return x + y

print(sum(1,2))
answer = sum (5,4)
print(f"The answer is {answer}")
