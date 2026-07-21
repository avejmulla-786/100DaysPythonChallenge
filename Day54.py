# Operator Overloading

class vector:
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k

    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"

    def __add__(self, x):
        return vector(
            self.i + x.i,
            self.j + x.j,
            self.k + x.k
        )


v1 = vector(3, 5, 6)
print(v1)

v2 = vector(1, 2, 9)
print(v2)

print(v1 + v2)
print(type(v1 + v2))

print("-" * 30)

v4 = vector(10, 20, 30)
v5 = vector(5, 10, 15)

print("Vector 4:", v4)
print("Vector 5:", v5)

result = v4 + v5

print("New Vector:", result)
print("i value:", result.i)
print("j value:", result.j)
print("k value:", result.k)