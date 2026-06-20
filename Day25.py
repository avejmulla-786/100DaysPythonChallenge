dic = {
    344: "Avej",
    56: "Aman",
    678: "Zakir",
    567: "Nisha"
}
print(dic)
print(dic.keys)
print(dic.values())


# Accessing Values
print("Student 344:", dic[344])

# Looping Through Dictionary
for key in dic:
    print(f"Roll No: {key}, Name: {dic[key]}")

# Using items()
for key, value in dic.items():
    print(key, ":", value)

# Adding New Entry
dic[999] = "Rehan"
print("Updated Dictionary:", dic)

print("Total Entries:", len(dic))
