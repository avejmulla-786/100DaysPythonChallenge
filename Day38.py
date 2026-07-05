f = open("MY_File.txt", "r")
print(f.read())

print("\nReading line by line:")

for line in f:
    print(line.strip())

f.close()