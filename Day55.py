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
 
print("-" * 30)

dog2 = Dog("Rocky", "Labrador")
dog3 = Dog("Max", "Husky")

dogs = [dog, dog2, dog3]

print("Dog Details:")

for d in dogs:
    print(f"Name: {d.name}")
    print(f"Species: {d.species}")
    print(f"Breed: {d.breed}")
    d.make_sound()
    print("-" * 20)

print("Total Dogs:", len(dogs))
