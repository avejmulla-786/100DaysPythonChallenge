s ={2,4,2,6}
print(s)

info = {"carla",19,False,5.9,19}
print(info)

Avej = set()
print(type(Avej))

for value in info:
    print(value)

# Extra Set Operations

numbers = {10,20,30,40,50}

print("Original Set",numbers)

numbers.add(60)
print("After adding 60",numbers)

numbers.remove(20)
print("After removing 20",numbers)

print("Length of set:",len(numbers))

if 30 in numbers :
    print("30 is the present in the set")

else:
    print("30 is the not present in set")  

#Loop through set 
for num in numbers:  
    print("Number:",num)
      
