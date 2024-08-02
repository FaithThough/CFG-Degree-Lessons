#instance method
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        return f"{self.name} says woof!"

dog = Dog("Rex")
print(dog.bark())  # Output: Rex says woof!


#class method
class Dog:
    species = "Canis lupus familiaris"

    def __init__(self, name):
        self.name = name

    @classmethod
    def set_species(cls, species_name):
        cls.species = species_name

    def get_species(self):
        return f"{self.name} is a {self.species}"

# Using the class method
Dog.set_species("Canis Canis")
dog = Dog("Rex")
print(dog.get_species())  # Output: Rex is a Canis Canis



#static method
class Math:
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def subtract(x, y):
        return x - y

# Using the static methods
print(Math.add(5, 3))        # Output: 8
print(Math.subtract(10, 4))  # Output: 6
