# Flag
isSuccessful = False

def name_validation(name):
    if ',' not in name:
        raise ValueError("Incorrect input: missing ',' to seperate name and surname")

def age_validation(age):
    if age <= 0:
        raise ValueError("Only positive values are allowed")
    assert 12 < age <= 19

    return True

try:
    name = input("Enter your name and surname seperated by a comma: ")
    name_validation(name)
    age = int(input("Enter your age: "))
    age_validation(age)
except ValueError as ve:
    print(f"Invalid input {ve}")
except AssertionError as ae:
    print("Your age is not within the teenage category")
else:
    with open("registration-file.txt", "a+") as file:
        file.write(f"New member name: {name} and age: {age}. \n")
        isSuccessful = True
finally:
    if isSuccessful:
        print("Registration is completed.")
    else:
        print(f"Registration failed")




