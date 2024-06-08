import math
import datetime
import random
import string

# ---- EXERCISE 1 ----
# Ask the user for their preferred mode of travel, which country travelled recently and the number of
# countries they have visited Print the values entered and perform a simple calculation such as If you visit 3 more
# countries, you will have visited XXX countries

# REMEMBER: The input() always returns a string value!!!
# You should convert this string value to an integer with int()

preferred_mode_of_travel = input('What is your preferred mode of travel? ').lower()
country = input('What country have you travelled to most recently? ').capitalize()
countries_visited = int(input('What countries have you visited? '))

print(f'Your preferred mode of travel is {preferred_mode_of_travel}')
print(f'You recently visited {country}')

if countries_visited + 3 > 0:
    total_countries = countries_visited + 3
    print(f'If you visit 3 more countries, you will have visited {total_countries} countries in total')
else:
    print("You haven't visited any countries yet")

# ---- EXERCISE 2 ----
# You have friends at your house for dinner, and you've accidentally burnt the lasagne.
# Time to order pizza 🍕
# Write a program calculate how many pizzas you need to feed you and your friends
# """
# In the code, the factor of 0.5 can be used to estimate the number of pizzas needed based on the assumption that one
# pizza can feed two people.
# Therefore, each friend is considered to eat half a pizza.

friends = int(input('How many friends do you have? '))
pizza_required = friends * 0.5

if isinstance(pizza_required, float):
    round_up_pizza = math.ceil(pizza_required)
    print(f'The number of pizzas you should order is {round_up_pizza}')
else:
    print(f'The number of pizzas you should order is {pizza_required}')

# ---- EXERCISE 3 ----
# Consider an application for hospital
# Take inputs from the user for these details
# Patient_Name, Date_of_Birth, Gender, Admission_Date (current date/time - use datetime)

patient_name = input('What is the patients name? ')
date_of_birth = input('What is the patients date of birth DD-MM-YYYY? ')
gender = input('What is the patients gender? ')
current_datetime = datetime.datetime.now()
admission_date = current_datetime.strftime("%d-%m-%y")
print(f'Patient name: {patient_name} \n Date of birth: {date_of_birth} \n Gender: {gender} \n Admission date:{admission_date}')

# ---- EXERCISE 4 ----
#  Write a very simple encoding program that accepts a word from a user and encodes it
#  by wrapping each letter with some other letters (symbols).
#  HINT: User for in loop to iterate over each char in a word
word_to_encode = input('What word would you like to encode?')
encoded_word = ''

for letter in word_to_encode:
    # Generate a random symbol
    random_symbol = random.choice(string.punctuation)
    # Concatenate the random symbol for each letter
    wrapper_letter = random_symbol + letter + random_symbol
    encoded_word += wrapper_letter

print(f"Encoded word: {encoded_word}")


# ---- EXERCISE 5 ----
# Write a function to return the area of a circle
def area_of_circle(radius):
    area = 3.14 * radius
    print(f'The area of your circle is {area}')

area_of_circle(4)


# ---- EXERCISE 6 ----
# Revisit your EXERCISE 3.
# Create a function to calculate age from date of birth
# Print the user age
def age_calculator(admission_date, date_of_birth):
    # Convert strings to datetime objects
    admission_date = datetime.datetime.strptime(admission_date, "%d-%m-%y")
    date_of_birth = datetime.datetime.strptime(date_of_birth, "%d-%m-%Y")  # Note: capital Y for 4-digit year

    # Calculate age
    age = admission_date.year - date_of_birth.year - (
                (admission_date.month, admission_date.day) < (date_of_birth.month, date_of_birth.day))

    print(f"The patient is {age} years old.")

age_calculator(admission_date, date_of_birth)
