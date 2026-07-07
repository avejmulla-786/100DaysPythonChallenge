with open("MY_File.txt", "r") as f:

    print(type(f))

    # Move to the 10th byte
    f.seek(10)

    # Current position
    print("Current Position:", f.tell())

    # Read next 5 bytes
    data = f.read(5)
    print("Read Data:", data)

    # Current position after reading
    print("Position after reading:", f.tell())

    # Read remaining data
    remaining = f.read()
    print("Remaining Data:")
    print(remaining)

    print("Starting Position:", f.tell())

    first = f.read(8)
    print("First 8 Bytes:", first)

    print("Current Position:", f.tell())

    f.seek(0)
    print("After seek(0):", f.tell())

    print("First Line:", f.readline().strip())

    print("Current Position:", f.tell())