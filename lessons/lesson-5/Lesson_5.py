# Strings
# Sequence of characters
print("My name is Faith")
print("Faith"+" Phillips")
print("27")
print("24"+"3")

# Numbers
# Also known as integers
print(27)
print(24+1)

# Boolean
# Truthy or falsey values
print(True)
print(False)

# Methods
print("Faith".upper())
print("Faith".lower())
print("Faith".title())

# Variables
first_name = "Faith"
last_name = "Phillips"
age = 27
print(first_name)
print(last_name)
print(age)

print("Faith works as a developer")
print("Faith lives in Leeds")
print("Faith is 27 years old")
# We would have to manually change the value for every instance it occurs in

# Here we only have to change the variable once for it to change in every instance
first_name = "Eloise"
city = "London"
job = "software engineer"
print(first_name, "works as a", job)
print(first_name, "lives in", city)
print(first_name, "is 27 years old")

# Formatting strings
first_name = "Faith"
age = 27
city = "Leeds"
print(f"{first_name} is {age} years old and lives in {city}")

customer_name = "Marcus"
order = "watch"
date = "20-05-2024"
print(f"Hello {customer_name}, your {order} will be delivered to you by {date}. Thank you for your custom.")

# Format method
fruit = "mango"
print("My favourite fruit is {}.".format(fruit))

# Join method
fruits = ["mango", "strawberry", "guava"]
print(','.join(fruits))

# ASCII
print(ord("p"))
print(chr(86))

# String slicing
# [start(inclusive):stop(exclusive):step]
text = "Hello, world"
print(text[::2])
