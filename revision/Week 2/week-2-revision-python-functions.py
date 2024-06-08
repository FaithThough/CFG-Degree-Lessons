# # Functions we have already used
# print()
# input()

# Example function
# Defining a function
def greetings(name, age = 'unknown'): # parameter
    return(f'{name} is {age} years old')

# Calling a function
greetings('Marcus')
greetings('Lucy',22)

# Storing response in a variable
greetings_faith =  greetings('Faith', 27)
print(greetings_faith.upper())

def add(x=0,y=0):
    return x + y

print(add(2,3))
print(add())
print(add(2))

