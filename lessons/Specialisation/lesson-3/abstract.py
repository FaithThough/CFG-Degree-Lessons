# ABSTRACTION
"""
Refers to defining attributes/methods to be implemented later
"""

# Abstract class, gives you a method you need to define
# class Shape:
#     def calc_perimeter(self):
#         raise NotImplementedError("Please implement this method")
#
# #concrete class
# class Triangle(Shape):
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def calc_perimeter(self):
#         perim = self.a + self.b + self.c
#         print("Consider me implemented", perim)
#         return perim
#
# triangle_a = Triangle(5,5,5)
# triangle_a.calc_perimeter()
#

# METHOD TYPES
"""
Different ways to define methods within a class
"""

from datetime import date

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def details(cls, name, year):
        return cls(name, date.today().year - year)

    @staticmethod
    def check_age(age):
        return age > 18

person1 = Person("Jenny", 20)
person2 = Person.details("Fatima", 1992)

print(person1.name, person1.age)
print(person2.name, person2.age)

print(Person.check_age(33))




class CreditCardProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

    @abstractmethod
    def check_balance(self, amount):
        pass

    @abstractmethod
    def generate_receipt(self):
        pass