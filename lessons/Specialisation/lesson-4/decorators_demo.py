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

    return modified_function


def hello_world():
    print("Hello world👋🌍")


# # Approach 1: Manually decorating the function
# decorated_hello_world = decorator_function(hello_world)
# decorated_hello_world()

# Approach 2: using @ symbol
@decorator_function
def hello_world_decorated():
    print("Hello world👋🌍")


# Calling approach 2
hello_world_decorated()

def decorator_function(function):
    def modified_function(*args, **kwargs):
        print("Welcome to our application")
        function(*args, **kwargs)
        print("Thanks for visiting")

    return modified_function


@decorator_function
def hello_world_decorated(name):
    print(f"Hello {name}👋🌍")


# Calling the hello_world_decorated with an argument
hello_world_decorated("Faith")



# 4. Decorating Functions with Parameters
def validate_division(function):
    def modified_function(a, b):
        print(f"Let's divide {a} by {b}")
        if b == 0:
            print("You can't divide by zero ❌")
            return  # Return nothing (implicitly returns None) if b is 0 to prevent division by zero
        return function(a, b)  # Call the original function with the arguments a and b, and return its result

    return modified_function  # Return the modified_function so it replaces the original function when the decorator is applied


@validate_division
def divide(a, b):
    print(a / b)


divide(10, 5)
divide(3, 0)


# 5. Make general decorators that work with any number of parameters.
# ## Chain decorators together ###
def equal_sign(function):
    def modified_function(*args, **kwargs):
        print("=" * 40)
        function(*args, **kwargs)
        print("=" * 40)
    return modified_function


def pipe_sign(function):
    def modified_function(*args, **kwargs):
        print("|" * 40)
        function(*args, **kwargs)
        print("|" * 40)
    return modified_function

@equal_sign
@pipe_sign
def display_message(message):
    print(message)


display_message("Hello👋")


# 6. Class Decorator example with *args and **kwargs
class my_class_decorator:
    def __init__(self, function):
        self.function = function # Store the original function

    def __call__(self, *args, **kwargs):
        print("Do something before the function calls") # Pre-processing
        self.function(*args, **kwargs) # Call the original function with all arguments
        print("Do something after the function calls") # Post-processing

@my_class_decorator
def my_function(name, message):
    print(f"{name}, {message}")

my_function("Faith", "hello")

