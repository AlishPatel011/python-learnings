# Initial dictionary
x = {
    'name': ['alish', 'deep', 'dhruv', 'keval'],
    'age': [30, 56, 89, 69]
}

# Accessing age of 'alish'
print("Age of alish:", x['age'][x['name'].index('alish')])

# Print all ages
print("All ages:", x['age'])

# Add new key 'income'
x['income'] = [90000, 30000, 89000, 56000]
print("After adding income:", x)

# Delete 'name' key
del x['name']
print("After deleting 'name' key:", x)

# Dictionary values
print("Values in dictionary:", x.values())

# Dictionary keys
print("Keys in dictionary:", x.keys())

# Dictionary items (key-value pairs)
print("Key-value pairs:", x.items())

# Update an existing key
x['age'][1] = 60  # change Deep’s age
print("After updating Deep’s age:", x)

# Add new key using update()
x.update({'city': ['Surat', 'Mumbai', 'Delhi', 'Baroda']})
print("After adding city:", x)

# Pop a key
x.pop('city')
print("After popping city key:", x)

# Clear entire dictionary (optional)
# x.clear()
# print("After clearing:", x)
