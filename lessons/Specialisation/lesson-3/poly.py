"""
Polymorphism
In OOP, refers to the ability of an object to behave in multiple ways
There's 2 ways to do this, method-overloading and method overriding
"""


# METHOD OVERRIDING - a method with the same name in the child class as the parent
# but changing the definition of what the method does
class Vehicle:
    def print_details(self):
        print("This is parent Vehicle class method")


class Car(Vehicle):
    def print_details(self):
        print("This is child Car class method")


class Cycle(Vehicle):
    def print_details(self):
        print("This is child Cycle class method")

cycle_a = Cycle()

"""
METHOD OVERLOADING - when the method behaves in different ways, depending on the type or number of parameters
"""

class Car:
    def start(self, a, b=None):
        if b is not None:
            print(a+b)
        else:
            print(a)