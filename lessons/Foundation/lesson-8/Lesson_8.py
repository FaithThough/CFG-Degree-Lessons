# Lists
my_grocery = ["rice", "basil", "salmon", "chicken"]

print(my_grocery)
print(type(my_grocery))

# Functions
print(f"Total items in your list: {len(my_grocery)}")
print(f"Your sorted list: {sorted(my_grocery)}")
print(f"Your reversed list: {list(reversed(my_grocery))}")

# Conditional statements using IN operator
input_item = input("What else do you want to add to the list? ")
if input_item  in my_grocery:
    print(f"{input_item} is already in the list")
else:
    my_grocery.append(input_item)
    print(f"Your new item {input_item} has been added to the list")
print(f"Here is the updated list: {my_grocery}")

# my_grocery.clear()

# for loop
for items in my_grocery:
    print(items)