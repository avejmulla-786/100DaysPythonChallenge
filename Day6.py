# strings are immutable

a = "!!! Avej !!!!!!!!!Avej"

print(a)
print(a.upper())
print(a.lower())
print(a.rstrip("!"))
print(a.replace("Avej", "Adil"))
print(a.split(" "))

blogHeading = "introduction to js"
print(blogHeading.capitalize())

str1 = "Welcome to the Console!!!"

print(len(str1))
print(len(str1.center(50)))

print(str1.endswith("to", 4, 10))

# More String Methods

print(a.count("Avej"))
print(str1.startswith("Welcome"))

str2 = "Python123"
print(str2.isalnum())

str3 = "python"
print(str3.isalpha())

str4 = "hello world"
print(str4.title())

str5 = "PYTHON"
print(str5.isupper())

str6 = "python is easy"
print(str6.find("easy"))

str7 = "12345"
print(str7.isdigit())

name = "avej mulla"
print(name.title())