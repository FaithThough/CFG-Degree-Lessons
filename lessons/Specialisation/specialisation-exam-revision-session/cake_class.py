# Define a class called Cake
class Cake:
    # Initialise the class with some attributes
    def __init__(self, flavour, layers):
        self.flavour = flavour
        self.layers = layers
        self.decorations = []

    # A method to add decorations to the cake
    def add_decoration(self, decoration):
        self.decorations.append(decoration)


# Create an instance of the Cake class
birthday_cake = Cake("red velvet", 3)

# Add decoration to the birthday cake
birthday_cake.add_decoration("sprinkles")
print(birthday_cake.decorations)



class WeddingCake(Cake):
    def __init__(self, flavour, layers, tiers):
        super().__init__(flavour, layers)
        self.tiers = tiers

    def describe(self):
        super().describe()
        print(f"This wedding cake has {self.tiers} tiers.")

    def add_decoration(self, decoration):
        if decoration == "figurine":
            self.decorations.append("special " + decoration)
        else:
            super().add_decoration(decoration)
