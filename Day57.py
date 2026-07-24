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