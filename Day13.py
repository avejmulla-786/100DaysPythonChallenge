def calculateGmean(a, b):
    mean = (a * b) / (a + b)
    print("Geometric Mean is:", mean)


def isGreater(a, b):
    if(a > b):
        print("First number is greater")

    else:
        print("Second number is greater or equal")


def isLesser(a, b):
    pass


a = 9
b = 8

isGreater(a, b)
calculateGmean(a, b)


# Extra Functions

def addition(x, y):
    print("Addition =", x + y)


def subtraction(x, y):
    print("Subtraction =", x - y)


addition(a, b)
subtraction(a, b)
print("Program executed successfully ")