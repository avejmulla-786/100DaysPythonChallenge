# Exception Handling in python
a = input("Enter the no")
print(f"Multiplication table of{a}is:")

try:
   for i in range(1,11):
      print(f"{int(a)} x = {int(a)*i}")
except :
   print("Invalid input!:")

print("Some lines of code") 
print("End of program")   
             
# Extra Exception Example

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    print("Division =", num1 / num2)

except ZeroDivisionError:
    print("Cannot divide by zero!")

except ValueError:
    print("Please enter only numbers!")
         
