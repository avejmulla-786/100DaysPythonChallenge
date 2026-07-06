# Reading File using readline()

f = open("MY_file.txt", "r")

line_no = 1

while True:
    line = f.readline()

    if not line:
        break

    print(f"Line {line_no}: {line.strip()}")

    # Count words in each line
    words = line.split()
    print("Total Words:", len(words))

    # Count characters
    print("Total Characters:", len(line.strip()))

    # Check if line is empty
    if line.strip() == "":
        print("This is an empty line.")
    else:
        print("This line contains text.")

    print("-" * 40)

    line_no += 1

f.close()
