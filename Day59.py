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

print("-" * 40)

print("Your Favourite Foods:")

for index, food in enumerate(foods, start=1):
    print(f"{index}. {food}")

print("Total Foods:", len(foods))

print("-" * 40)

# Another Walrus Operator Example

values = [10, 20, 30, 40, 50]

while (length := len(values)) > 0:
    print(f"Items remaining: {length}")
    removed = values.pop()
    print(f"Removed: {removed}")

print("-" * 40)

# Walrus with if statement

text = "Python Programming"

if (size := len(text)) > 10:
    print(f"Text is long. It contains {size} characters.")

    