""" Write a function that will take two whole numbers (integers) as input and output.
The function returns the result of multiplying these two numbers together. For example 5 * 4 = 20
However, to make this task more challenging, you have to assume the * key of your keyboard is broken
or missing and hence you are not allowed to use the * operator in your code!!! """

def add(a,b):
    total=0
    for x in range(a):
        total=total+b
    return total

print(add(5,10))

