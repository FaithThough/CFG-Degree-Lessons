# Opening and writing on a file
file = open("lesson-9-example.txt", "w")

# Using a variable means we can reuse without writing the whole thing
file.write("I can create and write on a file without even opening it.")
# If you don't explicitly close the file it will use your computer resources
file.close()

# Writing to the file
file = open("lesson-9-example.txt", "a")
file.write("\nI want to write something new to my file.")
file.close()

# Reading the file
file = open("lesson-9-example.txt", "r")
print(file.read())
file.close()

# Alternative reading of the file
with open("lesson-9-example.txt", "r") as a_file:
    print(a_file.read())

# Alternative writing to the file
with open("lesson-9-example.txt", "w") as a_file:
    a_file.write("Faith")

with open("lesson-9-example.txt", "a") as a_file:
    a_file.write("\nMarcus")

# Writing a list of strings to the file
lines = ["\nAaron ", "\nAmy ", "\nLauren "]
with open("lesson-9-example.txt", "a") as a_file:
    a_file.writelines(lines)

''' 
Exercise 1
Create a to-do list program that writes user input to a file
Ask the user to input a new to-do item
Read the contents of the existing to-do items
Add the new to-do item to the existing to-do items
Save the updated to-do items
You will need to manually create a new file called to-do.txt
'''
#
# with open("lesson-9-to-do.txt", "a") as a_file:
#     new_item = input("What would you like to add to your to-do list? ")
#     a_file.write(new_item + "\n")
#
# with open("lesson-9-to-do.txt", "r") as a_file:
#     print("Your to-do list:")
#     print(a_file.read())

# CSV files
import csv
a_header = ["item", "price"]
data = [
    {'item': 'Pasta', 'price': 3},
    {'item': 'Pizza', 'price': 2}
]

with open("lesson-9-menu.csv", "w", newline='') as csv_file:
    menu = csv.DictWriter(csv_file, fieldnames=a_header)
    menu.writeheader()
    menu.writerows(data)

with open("lesson-9-menu.csv", "r") as csv_file:
    csv_file_data = csv.DictReader(csv_file)
    for row in csv_file_data:
        print(row)