# Creating a file and adding to it
# with open("greek-menu.txt", "w") as menu:
#     dish = "dolmades"
#     menu.write(dish)
import csv

# Reading a file
with open("greek-menu.txt", "r") as menu:
    print(menu.read())

# # Creating a csv file
import csv
# Define column names
field_names = ["Dish", "Price"]

# Open the CSV file in write mode
with open("greek-menu.csv", "w", newline= '') as menu:
    # Create a DictWriter object and write the header
    writer = csv.DictWriter(menu, fieldnames= field_names)
    writer.writeheader()

    # Write initial data
    initial_data = [
        {"Dish": "Moussaka", "Price": "14.99"},
        {"Dish": "Souvlaki Platter", "Price": "12.49"},
        {"Dish": "Spanakopita", "Price": "7.99"},
        {"Dish": "Gyro Wrap", "Price": "9.49"},
        {"Dish": "Greek Salad", "Price": "8.99"},
        {"Dish": "Dolmades", "Price": "6.99"},
        {"Dish": "Baklava", "Price": "5.49"},
        {"Dish": "Calamari", "Price": "10.99"},
        {"Dish": "Tzatziki & Pita", "Price": "4.99"},
        {"Dish": "Lamb Chops", "Price": "18.99"}
    ]

    # Write the initial data to the csv file
    for row in initial_data:
        writer.writerow((row))

# Reading the csv file
with open("greek-menu.csv", "r") as menu:
    menu_reader = csv.DictReader(menu)
    for row in menu_reader:
        print(dict(row))


