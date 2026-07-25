import time

def usingWhile():
    i = 0
    while i<500:
        i = i + 1
        print(i)

def usingFor():
    for i in range(500):
        print(i)

init = time.time()
usingFor()
print(time.time() - init)
t1 = init = time.time()
usingWhile()
print(time.time() - init)
print(t1)

print("-" * 40)

# More Time Module Practice

current_time = time.time()
print("Current Timestamp:", current_time)

print("-" * 40)

# Measure a simple task

start = time.time()

total = 0

for i in range(1, 10001):
    total = total + i

end = time.time()

print("Sum:", total)
print("Execution Time:", end - start)

print("-" * 40)

# Sleep Function

print("Program Started")

time.sleep(2)

print("2 Seconds Completed")

print("-" * 40)

# Current Date and Time

current = time.ctime()

print("Current Date and Time:", current)

