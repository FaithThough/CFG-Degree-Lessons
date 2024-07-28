# class Animal:
#     pass

# Initial Dog class (not inheriting from Animal)
class Dog:
    # Class attributes
    number_of_legs = 4
    can_fly = False

    # Instance attributes
    def __init__(self, name, age, breed):
        self.name = name
        self.__age = age
        self.breed = breed

    def get_age(self):
        return self.__age

# Object
buddy = Dog("Buddy", "6 months", "Australian Shepherd")

# Retrieving data from object
# buddy.can_fly = True
print(buddy.can_fly)
print(buddy.number_of_legs)
print(buddy.get_age())

# New object
luna = Dog("Luna", "4 months", "Poodle")
print(luna.breed)

# Parent class
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print("Animal sound")

# Child class Dog inheriting from Animal
class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def speak(self):  # Overriding the base method
        print("Woof!")

# Child class Cat inheriting from Animal
class Cat(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def speak(self):  # Overriding the base method
        print("Meow!")


# Abstraction

from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof"

class Cat(Animal):
    def speak(self):
        return "Meow"
