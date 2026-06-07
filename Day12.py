for i in range(12):
   if(i == 10):
      break
   if(i == 5):
      print("Skip the iteration")
   print("5 X" , i+1 ," = " , 5 * (i+1))

print("exit the loop")   

# Extra Loop

for num in range(1, 6):
   print("Number:", num)

print("Second loop completed ")


# Even and Odd Check

for n in range(1, 11):

   if(n % 2 == 0):
      print(n, "is Even")

   else:
      print(n, "is Odd")

print("Even Odd loop completed ")


# Reverse Counting

for x in range(10, 0, -1):
   print("Countdown:", x)