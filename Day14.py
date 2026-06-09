def average(a,b):
   print("The average is :",(a+b)/2)
    
average(3,8)    

def multiple_no_average(*numbers):
    sum = 0
    for i in numbers:
       sum = sum + i
    print("Total Average is:",sum/len(numbers))

multiple_no_average(52,46,34,56,45,55)       
