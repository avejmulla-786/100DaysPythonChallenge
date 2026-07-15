class Employee:
    company = "Apple"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show(self):
        print(f"Name    : {self.name}")
        print(f"Company : {self.company}")
        print(f"Salary  : ₹{self.salary}")
        print("-" * 30)

    @classmethod
    def changeCompany(cls, newCompany):
        cls.company = newCompany


# Objects
e1 = Employee("Harry", 50000)
e2 = Employee("Avej", 70000)
e3 = Employee("Rehan", 65000)

print("Before Changing Company")
e1.show()
e2.show()
e3.show()

# Change company for all employees
Employee.changeCompany("Tesla")

print("After Changing Company")
e1.show()
e2.show()
e3.show()

print("Current Company:", Employee.company)