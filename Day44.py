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
    