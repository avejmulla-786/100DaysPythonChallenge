num = 18

if (num < 0):
    print("Number is negative.")

elif (num > 0):

    if (num <= 10):
        print("Number is between 1-10")

    elif (num > 10 and num <= 20):
        print("Number is between 11-20")

    else:
        print("Number is greater than 20")

else:
    print("Number is zero")






applePrice = 10
budget = 200

if (budget - applePrice > 50):
    print("Alexa, add 1 kg Apples to the cart.")

elif (budget - applePrice > 70):
    print("Its okay you can buy")

else:
    print("Alexa, do not add Apples to the cart.")    

print("Thank you for shopping with us!")
print("Visit again 😊")