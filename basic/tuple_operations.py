# Creating a tuple
my_tuple = (10, 20, 30, 40, 50)
print("Original Tuple:", my_tuple)

# Accessing elements
print("First element:", my_tuple[0])
print("Last element:", my_tuple[-1])

# Slicing
print("Sliced tuple (index 1 to 3):", my_tuple[1:4])

# Length of tuple
print("Length of tuple:", len(my_tuple))

# Nested tuple
nested = (1, 2, (3, 4), (5, (6, 7)))
print("Nested tuple:", nested)
print("Accessing nested value 7:", nested[3][1][1])

# Tuple with mixed data types
mixed = (100, "Alish", 10.5, True)
print("Mixed data type tuple:", mixed)

# Tuple unpacking
a, b, c, d = mixed
print("Unpacked values:", a, b, c, d)

# Tuple concatenation
t1 = (1, 2, 3)
t2 = (4, 5, 6)
t3 = t1 + t2
print("Concatenated tuple:", t3)

# Repeating tuples
t4 = ("Python",) * 3
print("Repeated tuple:", t4)

# Membership test
print("Is 20 in my_tuple?", 20 in my_tuple)
print("Is 99 not in my_tuple?", 99 not in my_tuple)

# Using count and index
sample = (10, 20, 20, 30, 20, 40)
print("Count of 20:", sample.count(20))
print("Index of first 30:", sample.index(30))

# Converting list to tuple
my_list = [1, 2, 3]
converted = tuple(my_list)
print("Converted from list:", converted)

# Min, max, sum (only if all elements are numbers)
nums = (5, 10, 3, 8)
print("Min:", min(nums))
print("Max:", max(nums))
print("Sum:", sum(nums))
