# Variable declaration and type checking
w = 10
print('Print variable:', w)
print('Type of variable:', type(w))

# More variables
a = 10.9
b = True
c = 'alish'
print('Types of a, b, c:', type(a), type(b), type(c))

# List creation
x = [10, 20, 30, 59, 90, 90.09, 79]
print('Type of x:', type(x))
print('Original list:', x)

# Append elements to the list
x.append(300)
x.append(29)
print('List after append:', x)

# Insert value at specific index
x.insert(2, 56)
print('List after inserting 56 at index 2:', x)

# Change value at a specific index
x[1] = 21
print('List after changing index 1 to 21:', x)

# Pop the last item
x.pop()
print('List after popping last item:', x)

# Minimum and maximum values
print('Minimum value in list:', min(x))
print('Maximum value in list:', max(x))

# Sort the list in ascending order
x.sort()
print('Sorted list (ascending):', x)

# Sort the list in descending order
x.sort(reverse=True)
print('Sorted list (descending):', x)

# Extend the list with another list
y = [10, 89, 63, 57]
print('Second list (y):', y)
x.extend(y)
print('List after extending with y:', x)

# Copy the list
z = x.copy()
print('Copied list (z):', z)

# Index of a specific value
index_val = x.index(56)  # Example: get index of value 56
print('Index of 56 in the list:', index_val)
