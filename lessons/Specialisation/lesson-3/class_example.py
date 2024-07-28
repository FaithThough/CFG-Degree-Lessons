# HOW TO CREATE A CLASS
# class Cat:
#     def __init__(self):
#         pass


# CREATED AN INSTANCE OF THE CAT CLASS
# jake = Cat()
# print(jake)

# ADD ATTRIBUTES TO CAT
# class Cat:
#     def __init__(self, name, age, breed):
#         self.name = name
#         self.age = age
#         self.breed = breed


# CREATED ANOTHER INSTANCE OF THE CAT CLASS
#
# jake = Cat('Jake', 5, 'Persian')
# print(jake.name + " is " + str(jake.age) + " years old.")

# ADD METHODS TO CAT
class Cat:
    def __init__(self, name, age, breed):
        self.friend = None
        self.name = name
        self.age = age
        self.breed = breed

    def meow(self):
        print("Meow Meow")

    def get_info(self):
        print(self.name + " is a " + str(self.age) + " years old " + self.breed + " cat.")

    def birthday(self):
        """
        add one year to the cat's age
        """
        self.age += 1

    def set_friend(self, friend):
        """
        new attribute to save friend object
        """
        self.friend = friend
        friend.friend = self


jake = Cat('Jake', 5, 'Persian')
jake.meow()
jake.get_info()

# create more cats
pippa = Cat("Pippa", 3, "Bengal")
snowy = Cat("Snowy", 8, "Siamese")
sparky = Cat("Sparky", 2, "Ragdoll")

pippa.get_info()
snowy.get_info()
sparky.get_info()

jake.birthday()
jake.get_info()

snowy.set_friend(sparky)

print(snowy.friend.name)

sparky.set_friend(pippa)

print(snowy.friend.name)