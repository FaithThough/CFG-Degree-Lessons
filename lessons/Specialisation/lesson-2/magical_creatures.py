class magical_creature:
    def __init__(self, name, species, magic_power, age):
        self.name = name
        self.species = species
        self.magic_power = magic_power
        self.age = age

    def use_power(self):
        return(f"{self.name} the {self.species} uses {self.magic_power}!")

    def grow_older(self):
        self.age += 1
        return(f"{self.name} is now {self.age} years old")


spark = magical_creature("Spark", "Dragon", "fire breathing", 300)
luna = magical_creature("Luna", "Unicorn", "healing", 150)
flare = magical_creature("Flare", "Phoenix", "teleportation", 500)

print(spark.use_power())
print(luna.grow_older())