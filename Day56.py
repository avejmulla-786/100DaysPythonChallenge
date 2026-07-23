# Multilevel Inheritance

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Species: {self.species}")


class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species="Dog")
        self.breed = breed

    def show_details(self):
        Animal.show_details(self)
        print(f"Breed: {self.breed}")


class GoldenRetriever(Dog):
    def __init__(self, name, color):
        Dog.__init__(self, name, breed="Golden Retriever")
        self.color = color

    def show_details(self):
        Dog.show_details(self)
        print(f"Color: {self.color}")


o = GoldenRetriever("Tommy", "Golden")

o.show_details()

print("-" * 30)

# Method Resolution Order
print(GoldenRetriever.mro())

print("-" * 30)

dog1 = GoldenRetriever("Bruno", "Light Golden")
dog2 = GoldenRetriever("Max", "Dark Golden")

dog1.show_details()

print("-" * 20)

dog2.show_details()

print("-" * 30)

dogs = [o, dog1, dog2]

for dog in dogs:
    print(f"{dog.name} is a {dog.breed} with {dog.color} color")

