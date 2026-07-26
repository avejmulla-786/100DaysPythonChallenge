# Walrus Operator
Happy = True
print(Happy)

print(Happy := True)
# using while loop 

numbers = [1, 2, 3, 4, 5]

while (n := len(numbers)) > 0 :
    print(numbers.pop())

foods = list()
# while True:
#     food = input("What food do you like?: ")
#     if food == "quit":
#         break
#     food.append(food)

# using Walrus Operator
while (food := input("what food do you like?:")) != "quit":
    foods.append(food)


    