class Dog:
    # class attributes
    num_of_legs = 4
    can_fly = False

    # instance attributes
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed


# Super class
class Bird:
    def fly(self):
        pass

class Sparrow(Bird):
    def fly(self):
        print("Sparrow is flying")

class Ostrich(Bird):
    def fly(self):
        raise NotImplementedError("Can't fly")


def make_bird_fly(bird):
    bird.fly()

make_bird_fly(Sparrow())
make_bird_fly(Ostrich())