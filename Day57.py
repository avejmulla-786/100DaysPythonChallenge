# Hybrid and Hierarchical Inheritance

class BaseClass:
    def show_base(self):
        print("This is Base Class")


class Derived1(BaseClass):
    def show_derived1(self):
        print("This is Derived Class 1")


class Derived2(BaseClass):
    def show_derived2(self):
        print("This is Derived Class 2")


class Derived3(Derived1, Derived2):
    def show_derived3(self):
        print("This is Derived Class 3")


obj = Derived3()

obj.show_base()
obj.show_derived1()
obj.show_derived2()
obj.show_derived3()

print("MRO:", Derived3.mro())
print("-" * 40)

# Hierarchical Inheritance

class Employee:
    def __init__(self, name):
        self.name = name

    def show_name(self):
        print(f"Employee Name: {self.name}")


class Developer(Employee):
    def coding(self):
        print(f"{self.name} works as a Developer")


class Designer(Employee):
    def designing(self):
        print(f"{self.name} works as a Designer")


class Manager(Employee):
    def managing(self):
        print(f"{self.name} works as a Manager")


dev = Developer("Avej")
designer = Designer("Aman")
manager = Manager("Rehan")

dev.show_name()
dev.coding()

print("-" * 20)

designer.show_name()
designer.designing()

print("-" * 20)

manager.show_name()
manager.managing()

