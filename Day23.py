ep1 = {122:45, 123:89, 567:69, 670:69}
ep2 = {222:67, 566:90}

print("Original Dictionary:", ep1)

ep1.update(ep2)
print("After Update:", ep1)

ep1.pop(122)
print("After Pop:", ep1)

ep1.popitem()
print("After Popitem:", ep1)

print("Keys:", ep1.keys())
print("Values:", ep1.values())

for key, value in ep1.items():
    print(f"Key = {key}, Value = {value}")


