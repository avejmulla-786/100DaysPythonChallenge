for i in range(5):
    print(i)
    i = i + 1
    # if i == 4:
    #  break 

else:
    print("Sorry no i")

for x in range(5):
    print("iterator no{}in for loop".format(x+1))
else:
    print("else bolck in loop")
print("out of the loop")         


for num in range(1, 6):
    print("Square of", num, "=", num * num)

else:
    print("Square loop ")




for letter in "Python":
    print(letter)

else:
    print("String loop ")



count = 1

while count <= 5:
    print("Count =", count)
    count += 1

else:
    print("While loop ")