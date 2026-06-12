countries = ("Spain","Italy","India","England","Germany")

temp = list(countries)
temp.append("Russia")
temp.pop(3)
temp[2] = "Finland"
countries = tuple(temp)
print(countries)

tuple = (0,1,2,3,2,3,1,3,2)