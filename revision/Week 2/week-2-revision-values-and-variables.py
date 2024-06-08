# Values
# Integer
32

# Float
3.2

# String
'Faith' # Single quotes
"Faith" # Double quotes
'''Faith''' # Triple quotes

# Outputting values
print(32)
print('Faith')

# Asking our user to type something
# input('What is your name? ')

# type()
print(type(32))
print(type(3.2))
print(type('Faith'))
print(type('32'))

# Integer vs strings
print(32+5)
print('32'+'5')
print(int("32")+int("5"))
print(type(str(32)))

# Variables
print('Marcus')
print('Marcus is a good student')
print('Marcus lives in Leeds')

name = 'Freya'
name = 'Khloe'
name = 'Faith'
age = 27
studying_field = 'programming'
print(name)
# String formatting
# f string
print(f'{name} is {age} years old')
# str.format method
print('{} is a good student in the field of {}'.format(name,studying_field))
# String concatenation
print(name,' lives in Leeds')

# Data manipulation
name = 'faith'
print(name.capitalize())