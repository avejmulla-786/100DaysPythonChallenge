def square(n):
    '''Takes in a number number,retuns the square of n'''
    print(n**2)
square(5)  
print(square.__doc__)

#temperature converter

def celsius_to_fahrenheit(c):
    '''Converts celsius to fahrenheit'''
    f = (c*9/5)+32
    print("Temperature in fahrenheit:",f)
celsius_to_fahrenheit(30)