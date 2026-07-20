class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id


class Programmer(Employee):
    def __init__(self, name, id, lang):
        super().__init__(name, id)
        self.lang = lang


rohan = Employee("Rohan Das", "420")
Avej = Programmer("Avej", "2345", "Python")

print(Avej.name)
print(Avej.id)
print(Avej.lang)

print("-" * 30)

# Creating more Programmer objects

p1 = Programmer("Aman", "5678", "Java")
p2 = Programmer("Rehan", "9876", "C++")

print("Programmer 1 Details:")
print("Name:", p1.name)
print("ID:", p1.id)
print("Language:", p1.lang)

print("-" * 30)

print("Programmer 2 Details:")
print("Name:", p2.name)
print("ID:", p2.id)
print("Language:", p2.lang)

print("-" * 30)

# Store programmers in a list

programmers = [Avej, p1, p2]

for programmer in programmers:
    print(f"{programmer.name} works with {programmer.lang}")

