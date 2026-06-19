cities = {"Tokyo","Madrid","Berlin","Delhi"}
cities2 = {"Seoul","kabul"}
print(cities.issuperset(cities2))
cities3 = {"Tokyo","Madrid","Delhi"}
print(cities.issuperset(cities3))
print(cities3.issubset(cities))


cities.add("Mumbai")
print("After Adding Mumbai:", cities)

cities.remove("Berlin")
print("After Removing Berlin:", cities)

common_cities = cities.intersection(cities3)
print("Common Cities:", common_cities)

all_cities = cities.union(cities2)
print("All Cities:", all_cities)
print("Total Cities:", len(cities))