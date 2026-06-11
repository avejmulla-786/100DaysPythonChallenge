tup = (1,2,76,342,32,"green")
print(tup[0])
print(tup[1])
print(tup[2])
print(tup[3])
print(tup[4])


if 342 in tup:
    print("Yes 342 is present in this tuple")


# Extra Tuple Operations

print("Length of tuple:", len(tup))

print("Last element:", tup[-1])

print("Tuple Slice:", tup[1:4])

for item in tup:
    print("Item:", item)
    
# Tuple Methods Practice

tup = (1, 2, 3, 4, 5)

print("Maximum:", max(tup))
print("Minimum:", min(tup))
print("Sum:", sum(tup))    