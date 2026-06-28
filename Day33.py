#Enumerate function
a = [12,56,32,98,12,45,1,4]

for index,mark in enumerate(a):
    print(mark)
# Starting index from 1

print("Enumerate Starting from 1")

for index,mark in enumerate(a,start=1):
    print(f"{index}.{mark}")

print("-" * 40)

# Finding values greater than 40 

for index, value in enumerate(a):
    if value > 40 :
       print(f"Value{value}found at index{index}")

print("-" * 40)

#Enumerate with string
name = "python"

for index,letter in enumerate (name,start=1):
    print(f"Character{index}:{letter}")