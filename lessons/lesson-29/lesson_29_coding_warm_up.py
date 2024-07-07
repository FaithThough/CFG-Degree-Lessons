""" Write a function that will take two whole numbers (integers) as input and output.
The function returns the result of multiplying these two numbers together. For example 5 * 4 = 20
However, to make this task more challenging, you have to assume the * key of your keyboard is broken
or missing and hence you are not allowed to use the * operator in your code!!! """

def multiply(a,b):
    total= a / (1/b)
    return total

number_1 = int(input('Enter the first number: '))
number_2 = int(input('Enter the second number: '))

if number_1 ==0 or number_2 == 0:
    print('Invalid input')
else:
    result = multiply(number_1, number_2)
    print(int(result))




