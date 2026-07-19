class Shape:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def area(self):
        return self.x * self.y

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        super().__init__( radius,radius)

    def area(self):
        return 3.14 * super().area()
    
rec = Shape(3,5)
print(rec.area())


print("-" * 30)

# Creating Circle Object
circle = Circle(5)

print("Rectangle Area:", rec.area())
print("Circle Area:", circle.area())

# Creating More Shapes
rec2 = Shape(10, 4)
circle2 = Circle(7)

print("-" * 30)

print("Second Rectangle Area:", rec2.area())
print("Second Circle Area:", circle2.area())

print("-" * 30)

# Display Shape Information
shapes = [rec, circle, rec2, circle2]

for shape in shapes:
    print("Area:", shape.area())