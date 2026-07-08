double = lambda x: x*2
cube = lambda x: x*x*x
def appl(fx,value):
    return 6 + fx(value)

avg = lambda x,y,z:(x+y+z)/3
     
print(double(5))
print(cube(5))
print(appl(cube,2))
print(appl(lambda x: x * x * x,2))
print(avg(5,6,7))
