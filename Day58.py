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

