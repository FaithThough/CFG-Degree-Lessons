
# Printing all of the even numbers from 2 to 100
# Less efficient: loops 100 times
def print_even_numbers_version_one():
    number = 2
    while number < 100:
        if number % 2 == 0:
            print(number)
        number += 1

# More efficient: loops 100 times
def print_even_numbers_version_two():
    number = 2
    while number < 100:
        print(number)
        number += 2

