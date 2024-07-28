# List
# italian_menu = ['pizza', 'spaghetti carbonara', 'caprese salad', 'mushroom risotto', 'lasagna', 'tiramisu', 'bruschetta', 'truffle ravioli', 'gelato']

# Dictionary
italian_menu = {
'pizza':12,
'spaghetti carbonara':14,
'caprese salad': 9,
'mushroom risotto': 16,
'lasagna': 17,
'tiramisu': 7,
'bruschetta': 7,
'truffle ravioli': 20,
'gelato': 5,
}
print(italian_menu)
print(italian_menu['pizza'])
print(italian_menu['spaghetti carbonara'])

for item, value in italian_menu.items():
    print(item, value)

# Adding items to a dictionary
italian_menu['fettuccine alfredo'] = 14
print(italian_menu)

# Updating values in a dictionary
italian_menu['gelato'] = 6
print(italian_menu)