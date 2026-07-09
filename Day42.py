#Map,Filter and reduce 
def cube(x):
    return x*x*x

print(cube(2))
l = [1,2,4,6,4,3]
# newl = []
# for item in l:
#     newl.append(cube(item))

newl = list(map(cube,l))    
print(newl)

#Filter
def filter_function(a):
    return a>2

newnewl = list(filter(filter_function,l))
print(newnewl)


# Square using lambda
square_list = list(map(lambda x: x ** 2, l))
print("Square List:", square_list)

# Even Numbers
even_numbers = list(filter(lambda x: x % 2 == 0, l))
print("Even Numbers:", even_numbers)

# Reduce - Sum of all elements
total = reduce(lambda x, y: x + y, l)
print("Sum of List:", total)

# Reduce - Maximum Number
maximum = reduce(lambda x, y: x if x > y else y, l)
print("Maximum Number:", maximum)