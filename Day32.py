#short hand if else statements
a = 330
b = 3303
print("A")if a > b else print("=") if a==b else print("B")

c = print(9)if a<b else 0
print(c)


# Even or Odd

num = int(input("Enter a number: "))
print("Even") if num % 2 == 0 else print("Odd")


# Maximum Number

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print("Maximum =", x) if x > y else print("Maximum =", y)


# Voting Eligibility

age = int(input("Enter your age: "))

print("Eligible for Voting ✅") if age >= 18 else print("Not Eligible ")


# Positive or Negative

number = int(input("Enter any number: "))

print("Positive") if number > 0 else print("Negative") if number < 0 else print("Zero")

