class Person:

    def __init__(self,name,occ):
        print("Hey I am a person")
        self.name = name
        self.occ = occ

    def info(self):
        print(f"{self.name} is a {self.occ}")


a = Person("Avej","Devloper") 
a.info()           
b = Person("harry","HR")
b.info()

c = Person("Rehan", "Chemical Engineer")
d = Person("Aman", "Data Analyst")

c.info()
d.info()

people = [a, b, c, d]

print("\nPerson Details")

for person in people:
    print(f"Name       : {person.name}")
    print(f"Occupation : {person.occ}")
    print("-" * 30)

print("Total Persons:", len(people))