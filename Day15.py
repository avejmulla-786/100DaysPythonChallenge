marks = [3, 4, 6 , "Avej",True]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])
print(marks[0])  

if "6" in marks:
    print("Yes")
else:
    print("No")
    

# List Slicing
print(marks[1:4])

# Adding elements
marks.append("Python")
marks.append(99)

print("Updated List:", marks)

# Length of list
print("Length of list:", len(marks))

# Loop through list
for item in marks:
    print("Item:", item)  


# List Methods

numbers = [10, 20, 30, 40]

print(numbers)

numbers.append(50)
print("After append:", numbers)

numbers.insert(1, 15)
print("After insert:", numbers)

numbers.remove(30)
print("After remove:", numbers)

numbers.sort()
print("Sorted list:", numbers)

numbers.reverse()
print("Reverse list:", numbers)

print("Index of 20:", numbers.index(20))

print("Count of 40:", numbers.count(40))


# Extra List Practice

students = ["Avej", "Adil", "Ali"]

for student in students:
    print("Student Name:", student)


                