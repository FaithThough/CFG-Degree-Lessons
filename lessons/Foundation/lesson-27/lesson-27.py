# # Classes
# class Dog:
#     # Class attributes
#     number_of_legs = 4
#     can_fly = False
#     # Instance attributes
#     def __init__(self, name, age, breed):
#         self.name = name
#         self.age = age
#         self.breed = breed
#
#     def sing(self):
#         print(f"{self.name} sings the song of their people")
#
# # Instance of the dog class
# luna = Dog('Luna', '3', 'German Shepherd')
# print(luna.name)
# print(luna.age)
# print(luna.breed)
# luna.sing()
#
# jeff = Dog('Jeff', '4 months', 'chihuahua')
# print(jeff.name)
# print(jeff.number_of_legs)

# Want to create a class for cats but they have the same attributes as dogs, so creating a bigger class
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Inheritance
class Dog(Animal):
    def __init__(self, name, age, breed):
        super(). __init__(name,age)
        self.breed = breed

class Cat(Animal):
    def __init__(self, name, age, breed):
        super(). __init__(name,age)
        self.breed = breed

    def meows(self):
        return f"{self.name} says MEOW 😺"

class WhatsAppProfile:
    def __init__(self, username, phone_number, status="Hello, I am using WhatsApp", profile_picture=None):
        self.username = username
        self.phone_number = phone_number
        self.status = status
        self.profile_picture = profile_picture

    def update_status(self,new_status):
        self.status = new_status
        return self.status

Faith = WhatsAppProfile("Faith", "0712345678")

print(Faith.status)
print(Faith.update_status('I am at the gym💪'))
