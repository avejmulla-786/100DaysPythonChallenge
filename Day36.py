import os

if (not os.path.exists("data")):
    os.mkdir("data")

for i in range(0,10):
    os.mkdir(f"data/Day{i+1}")


print("Current Directory:")
print(os.getcwd())

print("\nFolders inside data:")

for folder in os.listdir("data"):
    print(folder)    