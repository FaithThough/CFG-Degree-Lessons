# Good practice to put input in try block
try:
    number = int(input("Enter a number in the range of 5-10: "))
    if number <= 0:
        raise ValueError("Number shouldn't be 0 or a negative value")
    elif number < 5 or number > 10:
        raise ValueError("Your number is not in the requested range")
    answer = 100 / number
    print(f"{answer:.2f}")  # Format the answer to 2 decimal places)
    print("Division successful")

except ValueError as ve:
    print(ve)
