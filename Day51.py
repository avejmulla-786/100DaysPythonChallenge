class Employee:

    def __init__(self, name):
        self.name = name

    def __len__(self):
        i = 0
        for c in self.name:
            i = i + 1
        return i

    def __str__(self):
        return f"The name of the employee is {self.name}"


e = Employee("Avej")

print(e)
print(len(e))

print("-" * 40)

# Creating More Objects

e2 = Employee("Harry")
e3 = Employee("Rehan")

print(e2)
print("Length:", len(e2))

print("-" * 20)

print(e3)
print("Length:", len(e3))

print("-" * 40)

employees = [e, e2, e3]

print("Employee Details")

for emp in employees:
    print(emp)
    print("Name Length:", len(emp))
    print("-" * 20)

print("Total Employees:", len(employees))

