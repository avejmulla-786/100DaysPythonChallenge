#Global And Local

x = 4
print(x)

def hello():
    x = 5
    print(f"The Local {x}")
    print("Hello Avej")

print(f"The Global x is {x}")
hello()
x = 5
print(f"The Global x is {x}")