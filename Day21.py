#factorial 
def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(5))    

# Sum of Natural Numbers using Recursion

def natural_sum(n):
    if(n == 0):
        return 0
    else:
        return n + natural_sum(n-1)
print("sum of natural number ",natural_sum(12))   