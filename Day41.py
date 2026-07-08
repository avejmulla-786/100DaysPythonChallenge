double = lambda x: x*2
cube = lambda x: x*x*x
def appl(fx,value):
    return 6 + fx(value)

avg = lambda x,y,z:(x+y+z)/3
     
print("double",double(5))
print("cube of ",cube(5))
print(appl(cube,2))
print(appl(lambda x: x * x * x,2))
print("avg of 3 no",avg(5,6,7))


# More Lambda Function Examples
# -----------------------------

square = lambda x: x ** 2
print("Square of 8:", square(8))

addition = lambda a, b: a + b
print("Addition:", addition(15, 25))

maximum = lambda a, b: a if a > b else b
print("Maximum Number:", maximum(45, 67))

numbers = [2, 4, 6, 8, 10]

doubled_numbers = list(map(lambda x: x * 2, numbers))
print("Doubled List:", doubled_numbers)