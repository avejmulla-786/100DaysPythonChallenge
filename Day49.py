class Employee:
    def __init__(self,name ,salary):
       self.name = name
       self.salary = salary

    @classmethod
    def fromStr(cls,string):
        return cls(string.split("-")[0],string.split("-")[1])
    

e1 = Employee("Avej",12000)
print(e1.name)
print(e1.salary)       

print("-"*5)

# using class method 

string = "harry-10000"
e2 = Employee.fromStr(string)
print(e2.name)
print(e2.salary)
print("-" * 30)

# Creating more objects using fromStr()

string1 = "Rehan-25000"
string2 = "Aman-30000"
string3 = "Zakir-45000"

e3 = Employee.fromStr(string1)
e4 = Employee.fromStr(string2)
e5 = Employee.fromStr(string3)

print(e3.name)
print(e3.salary)

print(e4.name)
print(e4.salary)

print(e5.name)
print(e5.salary)

print("-" * 30)

employees = [e1, e2, e3, e4, e5]

print("Employee Details")

for emp in employees:
    print(f"Name   : {emp.name}")
    print(f"Salary : ₹{emp.salary}")
    print("-" * 20)

print("Total Employees:", len(employees))


