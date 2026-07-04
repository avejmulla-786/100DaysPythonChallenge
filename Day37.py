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

# Global Variable

x = 4
name = "Avej"

print("Global x =", x)
print("Name =", name)


def hello():
    # Local Variable
    x = 5
    language = "Python"

    print("\nInside hello()")
    print("Local x =", x)
    print("Learning:", language)


hello()

print("\nOutside Function")
print("Global x =", x)


# Using global keyword

count = 10

def update():
    global count
    count = count + 5
    print("Updated Count =", count)

update()

print("Final Global Count =", count)