print("=" * 50)
print("      STUDENT RESULT MANAGEMENT SYSTEM")
print("=" * 50)

name = input("Enter Student Name: ")

python = int(input("Enter Python Marks: "))
java = int(input("Enter Java Marks: "))
maths = int(input("Enter Maths Marks: "))
english = int(input("Enter English Marks: "))
science = int(input("Enter Science Marks: "))

total = python + java + maths + english + science
percentage = total / 5

print("\n" + "=" * 50)
print("             RESULT")
print("=" * 50)

print("Student Name :", name)
print("Total Marks  :", total, "/500")
print("Percentage   :", percentage, "%")

if percentage >= 90:
    grade = "A+"

elif percentage >= 80:
    grade = "A"

elif percentage >= 70:
    grade = "B"

elif percentage >= 60:
    grade = "C"

elif percentage >= 35:
    grade = "D"

else:
    grade = "F"

print("Grade        :", grade)

if grade == "F":
    print("Result       : FAIL ")
else:
    print("Result       : PASS ")

print("=" * 50)
print("Thank You!")