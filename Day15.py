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