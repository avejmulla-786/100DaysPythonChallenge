a = int(input("Enter any value between 5 and 9:"))

if(a<5 or a>9):
    raise ValueError("value should be between 5 and 9")



# Age Validation

age = int(input("Enter your age: "))

if(age < 18):
    raise Exception("You are not eligible to vote")

else:
    print("You are eligible to vote ")


# Marks Validation

marks = int(input("Enter your marks: "))

if(marks < 0 or marks > 100):
    raise ValueError("Marks should be between 0 and 100")

else:
    print("Marks accepted ")