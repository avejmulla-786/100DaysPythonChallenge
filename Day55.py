# Single Inheritance

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        print("Animal makes a sound")


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Dog")
        self.breed = breed

    def make_sound(self):
        print("Dog says: Woof Woof!")


animal = Animal("Leo", "Lion")

print("Name:", animal.name)
print("Species:", animal.species)
animal.make_sound()

print("-" * 30)

dog = Dog("Bruno", "German Shepherd")

print("Name:", dog.name)
print("Species:", dog.species)
print("Breed:", dog.breed)

dog.make_sound()