class Person:
    def __init__(self, name, age, occupation):
        self.name = name
        self.age = age
        self.occupation = occupation

    def __hash__(self):
        return hash((self.name, self.age, self.occupation))

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age and self.occupation == other.occupation

person_1 = Person("Faith",27,"Graduate Software Engineer")
person_2 = Person("Marcus", 29, "Senior Data Engineer")

hash_table = {person_1: "Birmingham", person_2: "London"}
print(hash(person_1))
print(hash(person_2))
print(hash_table[person_1])
print(hash_table[person_2])

