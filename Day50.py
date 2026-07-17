class Person:
    def __init__(self,name,age):
        self.name = name 
        self.age = age
        self.version = 1 


p = Person("John",30)
print(p.__dict__)

print(help(Person))

print("-" * 40)

# Adding a new attribute dynamically
p.city = "Pune"

print("Updated Dictionary:")
print(p.__dict__)

print("-" * 40)

# Creating another object
p2 = Person("Harry", 25)

print("Second Person Details:")
print(p2.__dict__)

print("-" * 40)

# Display object data
print(f"Name : {p.name}")
print(f"Age  : {p.age}")
print(f"City : {p.city}")