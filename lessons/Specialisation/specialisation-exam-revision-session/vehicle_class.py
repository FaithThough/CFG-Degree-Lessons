# OOP inheritance
class Vehicle:
    def __init__(self, make, colour):
        self.make = make
        self.colour = colour

    def driving(self):
        print("By default it is on four wheels 🚗")

# Design a child class of Vehicle called Motorcycle
# Needs to override diving (2 wheels)
# Create a new method called coolFactor
class Motorcycle(Vehicle):
    def driving(self):
        print("By default it is on two wheels🏍️")
    def coolFactor(self):
        print("It has a cool factor of 100😎")

# Design a  child class of Vehicle called Unicycle
# Needs to override driving (1 wheel)
# Create a new attribute - antique
# Create a new method called coolFactor

class Unicycle(Vehicle):
    def __init__(self, make, colour, antique=False):
        super().__init__(make,colour)
        self.antique = antique
    def driving(self, make, colour):
        print(f"The {self.colour} {self.make} unicycle is on one wheel1️⃣")

    def coolFactor(self):
        if self.antique:
            print("It has a unique cool factor")
        else:
            print("It has a cool factor")

vehicle1 = Vehicle("Audi", "White")
vehicle1.driving()

motorcycle = Motorcycle("Harley", "Yellow")
motorcycle.driving()

unicycle = Unicycle("Oracle", "Purple", antique=True)
unicycle.coolFactor()



