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