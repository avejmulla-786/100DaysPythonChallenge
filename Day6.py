# strings are immutable
a = "!!! Avej !!!!!!!!!Avej"
print(a)
print(a.upper())
print(a.lower())
print(a.rstrip(""))
print(a.replace("Avej","Adil"))
print(a.split(" "))

blogHeading = "introduction to js"
print(blogHeading.capitalize)


str1 = "Welcome to the Console!!!"
print(len(str1))
print(len(str1.center(50)))

print(str1.endswith("to",4,10))

str1 = "he's name is Dan. He is an honest man ."

print(str1.find("ishh"))
print(str1.index("ishh"))
