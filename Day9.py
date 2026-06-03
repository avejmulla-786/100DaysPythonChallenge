x = int(input("Enter the value of x: "))

# x is the variable to match
match x:

    # if x is 0
    case 0:
        print("x is zero")

    case 4:
        print("case is 4")

    case 10:
        print("x is ten")

    case 20:
        print("x is twenty")

    case _ if x < 0:
        print("Negative number entered")

    case _ if x % 2 == 0:
        print(x, "is an even number")

    case _ if x % 2 != 0:
        print(x, "is an odd number")

    case _ if x != 90:
        print(x, "is not 90")

    case _ if x != 80:
        print(x, "is not 80")

    case _:
        print(x)
        print("Default case executed")

print("Program executed successfully ✅")
print("Thanks for using Match Case in Python 🚀")