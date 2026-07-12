class Student:
    name = "Avej"
    Education = "Student"
    def info(self):
        print(f"{self.name} is a {self.Education}")

a = Student()
b = Student()
a.name = "Shubham" 
b.name = "Sumit"
a.Education = "MBBS"
b.Education = "Engineer"
a.info()
b.info()       
    
c = Student()
c.name = "Rehan"
c.Education = "chemical Engineer"

c.info()

print("\nStudent Details")

students = [a,b,c]

for student in students:
    print(f"name:{student.name}")
    print(f"Education:{student.Education}")
    print("-"*30)

print("Total Students:",len(students))




