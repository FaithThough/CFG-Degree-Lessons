# 1. Functions can be **passed as arguments** to another function object.
def increment_number(a):
    return a + 1


def decrement_number(a):
    return a - 1


print(increment_number(5))  # output: 6
print(decrement_number(6))  # output: 5


def operation(function, x):
    result = function(x)
    return result


print(operation(increment_number, 5))  # output: 6
print(operation(decrement_number, 6))  # output : 5


# 2. A function can **return another function**
# Nested function
def outer_function():
    print("This is the outer function")

    def inner_function():
        print("This is the inner function")

    return inner_function()  # Approach 1 requires (), approach 2 requires no ()
    # () calls the function


# Approach 1
outer_function()


# Approach 2
# calling_function = outer_function()
# calling_function()

# 3. A decorator takes in a function, adds some functionality and returns it
def decorator_function(function):
    def modified_function():
        print("Welcome to our application")
        function()
        print("Thanks for visiting")

    return modified_function()


def hello_world():
    print("Hello world👋🌍")


decorate = decorator_function(hello_world)
print(decorate)

# 4. Decorating Functions with Parameters

# 5. Make general decorators that work with any number of parameters.
# ## Chain decorators together ###

# 6. Class Decorator example with *args and **kwargs
