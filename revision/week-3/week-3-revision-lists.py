# Lists
# Inefficient way of saving students names
student = 'Faith'
student_2 = 'Marcus'
student_3 = 'Luna'

# Saving students name in a list
students = ["Faith","Marcus","Luna"]
print(students)

# Retrieving selected values
print(students[0])

# For loop to iterate over student name
for student in students:
    print(student)

fruits = ['mango', 'peach', 'strawberry', 'kiwi']
print(type(fruits))

# List methods
# Adding a value
fruits.append('banana')
print(fruits)

# Adding a value in a specific position
fruits.insert(1,'lychee')
fruits.insert(2, 'lychee')
print(fruits)

# Deleting the last value from the list
fruits.pop()
print(fruits)

# Deleting a value in a specific position
fruits.pop(0)
print(fruits)

# Removing the first occurance of something in a list
fruits.remove('lychee')
print(fruits)

# Sorting items in a list
fruits.sort()
print(fruits)

# Reversing the order of items in a list
fruits.reverse()
print(fruits)

# Copying items in a list
copied_fruits = fruits.copy()
print(copied_fruits)



